from flaskDir import db,app
from sqlalchemy import text

class DocumentoSanitarioDAO:
    __table="documentosanitario"
    @classmethod
    def doSave(cls,doc, titolare):
        query = text("INSERT INTO "+cls.__table+" VALUES(:id, :tipo,:dataem, :titolare)")
        if cls.findById(doc.getId()) is None:
            with app.app_context():
                db.session.execute(query,{"id": doc.getId(),"tipo": doc.getTipo(), "dataem": doc.getDataEmissione(), "titolare": titolare})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_doc, new_doc,titolare):
        query = text("UPDATE "+cls.__table+" SET ID=:id, tipo=:tipo, dataEmissione=:date, titolare=:titolare where ID=:old_id")
        if cls.findById(old_doc.getId()) is not None:
            with app.app_context():
                db.session.execute(query, {"id": new_doc.getId(), "tipo": new_doc.getTipo(), "date": new_doc.getDataEmissione(),
                                           "titolare": titolare, "old_id": old_doc.getId()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls, id):
        query = text("DELETE FROM "+cls.__table+" WHERE ID=:id")
        if cls.findById(id) is not None:
            with app.app_context():
                db.session.execute(query, {"id":id})
                db.session.commit()
            return True
        return False

    @classmethod
    def findById(cls,id=None):
        query = text("Select * from "+cls.__table+" where ID=:id")
        with app.app_context():
            if id is not None:
             return db.session.execute(query, {"id": id}).first()
    @classmethod
    def findByTitolare(cls,titolare=None):
        query = text("Select * from "+cls.__table+" where titolare=:titolare")
        if titolare is not None:
            with app.app_context():
                return db.session.execute(query, {"titolare": titolare}).all()
    @classmethod
    def findAll(cls):
        query = text("Select * from "+cls.__table)
        with app.app_context():
            return db.session.execute(query)

