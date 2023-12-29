from sqlalchemy import text
from flaskDir import db, app
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario

class EnteSanitarioDAO:
    __table="entesanitario"
    @classmethod
    def doSave(cls,new_ente: EnteSanitario)->bool:
        query=text("INSERT INTO "+cls.__table+" VALUES (:nome,:email,:password)")
        if EnteSanitarioDAO.findByEmail(new_ente.getEmail()) is None:
            with app.app_context():
                db.session.execute(query, {"nome": new_ente.getNome(), "email": new_ente.getEmail(), "password": new_ente.getPassword()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_email: str, new_name: str, new_email: str, new_password:str)->bool:
        query=text("UPDATE "+cls.__table+" SET nome=:nome, email=:email, password=:password WHERE email=:old")
        old_ente=EnteSanitarioDAO.findByEmail(old_email)
        if old_ente is not None:
            with app.app_context():
                db.session.execute(query, {"nome": new_name, "email": new_email, "password": new_password, "old": old_email})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls,email:str)->bool:
        query=text("DELETE FROM "+cls.__table+" WHERE email=:email")
        deletedEnte = EnteSanitarioDAO.findByEmail(email)
        if deletedEnte is not None:
            with app.app_context():
                db.session.execute(query, {"email": email})
                db.session.commit()
                return True
        return False

    @classmethod
    def findByEmail(cls,email:str)->EnteSanitario:
        query=text("Select * from "+cls.__table+" where email=:email")
        with app.app_context():
         res = db.session.execute(query, {"email": email}).first()
         ente=EnteSanitario(*res)
         return ente

    @classmethod
    def findAll(cls)->list:
        query=text("SELECT * from "+cls.__table)
        enti=list()
        with app.app_context():
            res = db.session.execute(query).all()
            if res is not None:
                for row in res:
                    ente=EnteSanitario(*row)
                    enti.append(ente)
        return enti






