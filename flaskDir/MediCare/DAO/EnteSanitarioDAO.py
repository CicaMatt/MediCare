from sqlalchemy import text
from flaskDir import db,EnteSanitario, app

class EnteSanitarioDAO:
    __table="ente_sanitario"
    @classmethod
    def doSave(cls,new_ente):
        query=text("INSERT INTO "+cls.__table+" VALUES (:nome,:email,:password)")
        if EnteSanitarioDAO.findByEmail(new_ente.getEmail()) is None:
            with app.app_context():
                db.session.execute(query, {"nome": new_ente.getNome(), "email": new_ente.getEmail(), "password": new_ente.getPassword()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_email, new_name, new_email, new_password):
        query=text("UPDATE "+cls.__table+" SET nome=:nome, email=:email, password=:password WHERE email=:old")
        old_ente=EnteSanitarioDAO.findByEmail(old_email)
        if old_ente is not None:
            with app.app_context():
                db.session.execute(query, {"nome": new_name, "email": new_email, "password": new_password, "old": old_email})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls,email):
        query=text("DELETE FROM "+cls.__table+" WHERE email=:email")
        deletedEnte = EnteSanitarioDAO.findByEmail(email)
        if deletedEnte is not None:
            with app.app_context():
                db.session.execute(query, {"email": email})
                db.session.commit()
                return True
        return False

    @classmethod
    def findByEmail(cls,email):
        query=text("Select * from "+cls.__table+" where email=:email")
        with app.app_context():
         return db.session.execute(query, {"email": email}).first()
    @classmethod
    def findAll(cls):
        with app.app_context():
         return db.session.query(EnteSanitario).all()



enteSanitario=EnteSanitario(email="pinco",nome="pallino",password="ciao")
EnteSanitarioDAO.doSave(enteSanitario)
for el in EnteSanitarioDAO.findAll():
    print(el.email)

EnteSanitarioDAO.doUpdate("pinco","guido","dsf","pulcino")
for el in EnteSanitarioDAO.findAll():
    print(el.email)

