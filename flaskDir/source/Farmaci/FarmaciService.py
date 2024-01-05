import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.Farmaco import Farmaco

class FarmaciService:

    @classmethod
    def getFarmaci(cls):
        return db.session.scalars(sqlalchemy.select(Farmaco))

    @classmethod
    def getDettagliFarmaco(cls, id):
        return db.session.scalar(sqlalchemy.select(Farmaco).where(Farmaco.ID == id))

    @classmethod
    def getSuggeriti(cls, tipo, id):
        return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.categoria==tipo, Farmaco.ID != id))
