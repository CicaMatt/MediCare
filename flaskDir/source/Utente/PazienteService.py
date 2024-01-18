import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

from flaskDir import db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione


class PazienteService:

    @staticmethod
    def retrievePaziente(email, password):
        paziente = db.session.scalar(sqlalchemy.select(Paziente).where(Paziente.email == email))
        if paziente is None or not paziente.check_password(password):
            return None
        return paziente
    @classmethod
    def getListaVaccini(cls, user):
        return DocumentoSanitario.query.filter_by(titolare=user.CF, tipo="Vaccino").all()

    @classmethod
    def getListaPrenotazioni(cls, user):
        return db.session.scalars(sqlalchemy.select(Prenotazione).where(Prenotazione.pazienteCF == user.CF))


    @classmethod
    def eliminaPaziente(cls, cf):
        try:
            Prenotazione.query.filter_by(pazienteCF=cf).delete()
            DocumentoSanitario.query.filter_by(titolare=cf).delete()
            MetodoPagamento.query.filter_by(beneficiario=cf).delete()
            paziente = Paziente.query.filter_by(CF=cf).first()
            if paziente:
                db.session.delete(paziente)
                db.session.commit()
                return True
            else:
                return False

        except SQLAlchemyError as e:
            print("Errore durante l'eliminazione del paziente: {}".format(e))
            # Rollback in caso di errore
            db.session.rollback()
            return False