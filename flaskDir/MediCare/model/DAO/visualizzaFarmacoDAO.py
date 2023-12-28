from flaskDir import db, app
from sqlalchemy import text

class VisualizzaFarmacoDAO:
    __table="visualizzafarmaco"

    @classmethod
    def findByKey(cls, paziente=None, id_farm=None):
        query = text("Select * from "+cls.__table+" where Farmaco=:farm and Paziente=:visit")
        if id_farm is not None and paziente is not None:
            with app.app_context():
                return db.session.execute(query, {"farm":id_farm, "visit": paziente}).first()

    @classmethod
    def findById(cls,id=None):
        query = text("Select * from "+cls.__table+" where Farmaco=:farm")
        if id is not None:
            with app.app_context():
                return db.session.execute(query, {"farm": id}).all()

    @classmethod
    def findByPaziente(cls,paziente=None):
        query = text("Select * from "+cls.__table+" where Paziente=:paz")
        if paziente is not None:
            with app.app_context():
                return db.session.execute(query, {"paz": paziente}).all()
