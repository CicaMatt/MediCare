import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.Paziente import Paziente


class ISEEService:

    @classmethod
    def changeISEE(cls,cf,newIsee):
        paziente = Paziente.query.filter_by(CF=cf).first()

        if paziente:
            paziente.ISEE_ordinario=newIsee
            db.session.commit()












