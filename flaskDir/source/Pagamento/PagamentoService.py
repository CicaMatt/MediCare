import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db, app
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento

class PagamentoService:

    @classmethod
    def getMetodi(cls,cf):
        return db.session.scalars(sqlalchemy.select(MetodoPagamento).where(MetodoPagamento.beneficiario == cf))

    @classmethod
    def eliminaMetodo(cls,pan):
        carte_da_cancellare = MetodoPagamento.query.filter_by(PAN=pan).all()

        for metodo_pagamento in carte_da_cancellare:
            db.session.delete(metodo_pagamento)

        db.session.commit()

    @classmethod
    def addCarta(cls,cvv,pan,titolare,scadenza,cf):
        print("Service finito")
        with app.app_context():
            metodo=MetodoPagamento()
            metodo.CVV=cvv
            metodo.PAN=pan
            metodo.nome_titolare=titolare
            metodo.dataScadenza=scadenza
            metodo.beneficiario=cf
            db.session.add(metodo)
            db.session.commit()

