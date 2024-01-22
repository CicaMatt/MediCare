from datetime import datetime

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db, app
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente


class PagamentoService:

    @classmethod
    def getMetodi(cls, cf):
        """
        Restituisce la lista dei metodi di pagamento associati a un paziente.

        Args:
            cf (str): Codice fiscale del paziente.

        Returns:
            list: Lista dei metodi di pagamento associati al paziente.
        """
        return db.session.scalars(sqlalchemy.select(MetodoPagamento).where(MetodoPagamento.beneficiario == cf))

    @classmethod
    def eliminaMetodo(cls, pan, cf):
        """
        Elimina un metodo di pagamento associato a un paziente.

        Args:
            pan (str): Numero di carta del metodo di pagamento da eliminare.
            cf (str): Codice fiscale del paziente.

        Returns:
            None
        """
        carte_da_cancellare = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=cf).all()

        for metodo_pagamento in carte_da_cancellare:
            db.session.delete(metodo_pagamento)

        db.session.commit()

    @classmethod
    def addCarta(cls, cvv, pan, titolare, scadenza, cf):
        """
        Aggiunge un nuovo metodo di pagamento (carta di credito) associato a un paziente.

        Args:
            cvv (int): Codice di sicurezza della carta.
            pan (str): Numero di carta.
            titolare (str): Nome del titolare della carta.
            scadenza (str): Data di scadenza della carta nel formato 'MM/YYYY'.
            cf (str): Codice fiscale del paziente.

        Returns:
            bool: True se l'aggiunta è avvenuta con successo, False altrimenti.
        """
        with app.app_context():
            try:
                paziente = Paziente.query.filter(Paziente.CF == cf).first()

                try:
                    scadenza_date = datetime.strptime(scadenza, '%m/%Y')
                except ValueError:
                    return False

                if len(str(cvv)) != 3:
                    return False

                cartaEsistente = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=cf).first()
                if cartaEsistente:
                    return None
                else:
                    metodo = MetodoPagamento()
                    metodo.CVV = cvv
                    metodo.PAN = pan
                    metodo.nome_titolare = titolare
                    metodo.dataScadenza = scadenza_date.strftime('%m/%Y')
                    metodo.beneficiario = cf
                    metodo.paziente = paziente
                    db.session.add(metodo)
                    db.session.commit()
                    return True
            except SQLAlchemyError:
                return False
