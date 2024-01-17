import re

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario, Medico
from flaskDir import db, app
class EnteService:
    @staticmethod
    def retrieveEnte(email, password):
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email))
        if ente is None or not ente.check_password(password):
            return None
        return ente

    @staticmethod
    def creaReparto(nome,email,password,specializzazione,citta,ente):
        formato_email=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not formato_email.match(email):return False
        if not 8<=len(password)<=20:return False
        with app.app_context():
            try:
                medico=Medico()
                medico.reparto=nome
                medico.email=email
                medico.set_password(password)
                medico.specializzazione=specializzazione
                medico.città=citta
                medico.tariffa=20.00
                medico.ente_sanitario=ente

                db.session.add(medico)
                db.session.commit()
                return True
            except SQLAlchemyError as e:
                return False


    @staticmethod
    def deleteReparto(email):
        with app.app_context():
            medico=db.session.scalar(sqlalchemy.select(Medico).where(Medico.email ==email))
            db.session.delete(medico)
            db.session.commit()
