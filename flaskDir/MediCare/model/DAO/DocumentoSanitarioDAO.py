from flaskDir import db,app
from sqlalchemy import text
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
class DocumentoSanitarioDAO:
    __table="documentosanitario"
    @classmethod
    def doSave(cls,doc: DocumentoSanitario)->bool:
        query = text("INSERT INTO "+cls.__table+" VALUES(:id, :tipo,:dataem,:desc, :titolare)")
        if cls.findById(doc.getId()) is None:
            with app.app_context():
                db.session.execute(query,{"id": doc.getId(),"tipo": doc.getTipo(), "dataem": doc.getDataEmissione(),"desc": doc.getDescrizione(),
                    "titolare": doc.getTitolare()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_doc:DocumentoSanitario, new_doc:DocumentoSanitario)->bool:
        query = text("UPDATE "+cls.__table+" SET NumeroDocumento=:id, tipo=:tipo, dataEmissione=:date,descrizione=:desc titolare=:titolare where NumeroDocumento=:old_id")
        if cls.findById(old_doc.getId()) is not None:
            with app.app_context():
                db.session.execute(query, {"id": new_doc.getId(), "tipo": new_doc.getTipo(), "date": new_doc.getDataEmissione(),
                                           "desc": new_doc.getTitolare(), "old_id": old_doc.getId()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls, id:str)->bool:
        query = text("DELETE FROM "+cls.__table+" WHERE NumeroDocumento=:id")
        if cls.findById(id) is not None:
            with app.app_context():
                db.session.execute(query, {"id":id})
                db.session.commit()
            return True
        return False

    @classmethod
    def findById(cls,id=None)->DocumentoSanitario:
        query = text("Select * from "+cls.__table+" where NumeroDocumento=:id")
        with app.app_context():
            if id is not None:
                res = db.session.execute(query, {"id": id}).first()
            if res is not None:
                document=DocumentoSanitario(*res)
                return document
    @classmethod
    def findByTitolare(cls,titolare=None)->list:
        query = text("Select * from "+cls.__table+" where titolare=:titolare")
        docs=list()
        if titolare is not None:
            with app.app_context():
                res = db.session.execute(query, {"titolare": titolare}).all()
                if res is not None:
                    for row in res:
                        doc=DocumentoSanitario(*row)
                        docs.append(doc)
        return docs
    @classmethod
    def findAll(cls)->list:
        query = text("Select * from "+cls.__table)
        docs=list()
        with app.app_context():
            res = db.session.execute(query).all()
            if res is not None:
                for row in res:
                    doc=DocumentoSanitario(*row)
                    docs.append(doc)
        return docs


