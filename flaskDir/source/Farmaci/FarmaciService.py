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
        if categoria is not None and prezzo > 2:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.prezzo<=prezzo, Farmaco.categoria==categoria))
        elif categoria is None:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.prezzo<=prezzo))
        elif prezzo == 2:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.categoria==categoria))
        else:
            return cls.getFarmaci()

    @classmethod
    def ricerca(cls,tip=None):
        if tip is not None and tip!="":
            suggerimenti={farmaco.nome for farmaco in Farmaco.query.filter(Farmaco.nome.like(tip+'%')).all()}
            suggest=list(suggerimenti)
            return suggest

    @classmethod
    def ricercaNome(cls, nome=None):
        if nome is not None:
            return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.nome==nome))





