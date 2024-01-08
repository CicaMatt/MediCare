import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento

class PagamentoService:

    @classmethod
    def getMetodi(cls,cf):
        return MetodoPagamento.query.filter_by(beneficiario=cf)

    @classmethod
    def eliminaMetodo(cls,pan):
        carte_da_cancellare = MetodoPagamento.query.filter_by(PAN=pan).all()

        for metodo_pagamento in carte_da_cancellare:
            db.session.delete(metodo_pagamento)

        db.session.commit()

    @classmethod
    def creaMetodo(cls, metodopagamento, cf):
        cls.listaCarte = cls.getMetodi(cls, cf)
        cls.listaCarte.append(metodopagamento)













