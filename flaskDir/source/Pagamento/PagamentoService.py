import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento

class PagamentoService:

    @classmethod
    def getMetodi(cls,cf):
        return MetodoPagamento.query.filter_by(beneficiario=cf)









