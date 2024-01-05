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

    @classmethod
    def filtraCatalogo(cls,categoria = None, prezzo=2):
        print(prezzo)
        if categoria is not None and prezzo > 2:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.prezzo<=prezzo, Farmaco.categoria==categoria))
        elif categoria is None:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.prezzo<=prezzo))
        elif prezzo == 2:
            print(categoria)
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.categoria==categoria))
        else:
            return cls.getFarmaci()


