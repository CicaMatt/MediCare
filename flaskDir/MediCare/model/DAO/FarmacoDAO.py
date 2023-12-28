from flaskDir import db, app
from sqlalchemy import text

class FarmacoDAO():
    __table="farmaco"


    @classmethod
    def doSave(cls,farmaco):
        query = text("INSERT INTO "+cls.__table+" VALUES(:prezzo, :nome, :descrizione)")
        if cls.findById(farmaco.id) is None:
            with app.app_context():
                db.session.execute(query,{"prezzo":farmaco.getPrezzo(), "nome":farmaco.getNome(), "descrizione":farmaco.getDescrizione()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_id,new_farmaco):
        query = text("UPDATE "+cls.__table+" SET prezzo=:prezzo, nome=:nome, descrizione=:descrizione WHERE ID=:id")
        if cls.findById(old_id) is not None:
            with app.app_context():
                db.session.execute(query,{"prezzo": new_farmaco.getPrezzo(), "nome": new_farmaco.getNome(), "descrizione": new_farmaco.getDescrizione()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls,id):
        query = text("DELETE FROM "+cls.__table+" WHERE id=:id")
        if cls.findById(id) is not None:
            with app.app_context():
                db.session.execute(query, {"id": id})
                db.session.commit()
            return True
        return False


    @classmethod
    def findById(cls, id):
        query = text("Select * from "+cls.__table+" where ID=:id")
        with app.app_context():
            return db.session.execute(query,{"id": id}).first()


    @classmethod
    def findAll(cls):
        query = text("SELECT * from "+cls.__table)
        with app.app_context():
            return db.session.execute(query)



