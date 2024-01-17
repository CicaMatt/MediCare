import sqlalchemy
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir import db
class EnteService:
    @staticmethod
    def retrieveEnte(email, password):
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email))
        if ente is None or not ente.check_password(password):
            return None
        return ente
