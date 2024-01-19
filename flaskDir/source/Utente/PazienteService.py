import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

from flaskDir import db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione


class PazienteService:

    @staticmethod
    def retrievePaziente(email, password):
        """
        Recupera un paziente dal database basandosi su email e password.

        Args:
        email (str): Indirizzo email del paziente.
        password (str): Password del paziente.

        Returns:
        Paziente or None: Oggetto Paziente se trovato, altrimenti None.
        """
        paziente = db.session.scalar(sqlalchemy.select(Paziente).where(Paziente.email == email))
        if paziente is None or not paziente.check_password(password):
            return None
        return paziente
    @classmethod
    def getListaVaccini(cls, user):
        """
        Ottiene la lista dei documenti sanitari di tipo "Vaccino" di un paziente.

        Args:
        user (Paziente): Oggetto Paziente.

        Returns:
        list: Lista dei documenti sanitari di tipo "Vaccino" del paziente.
        """
        return DocumentoSanitario.query.filter_by(titolare=user.CF, tipo="Vaccino").all()

    @classmethod
    def getListaPrenotazioni(cls, user):
        """
        Ottiene la lista delle prenotazioni di un paziente.

        Args:
        user (Paziente): Oggetto Paziente.

        Returns:
        list: Lista delle prenotazioni del paziente.
        """
        return db.session.scalars(sqlalchemy.select(Prenotazione).where(Prenotazione.pazienteCF == user.CF))


    @classmethod
    def eliminaPaziente(cls, cf):
        """
        Elimina un paziente dal database e tutti i suoi dati correlati.

        Args:
        cf (str): Codice fiscale del paziente.

        Returns:
        bool: True se l'eliminazione ha avuto successo, False altrimenti.
        """
        try:
            Prenotazione.query.filter_by(pazienteCF=cf).delete()
            DocumentoSanitario.query.filter_by(titolare=cf).delete()
            MetodoPagamento.query.filter_by(beneficiario=cf).delete()
            paziente = Paziente.query.filter_by(CF=cf).first()
            if paziente:
                db.session.delete(paziente)
                db.session.commit()
                return True
            else:
                return False

        except SQLAlchemyError as e:
            print("Errore durante l'eliminazione del paziente: {}".format(e))
            # Rollback in caso di errore
            db.session.rollback()
            return False