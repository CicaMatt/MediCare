import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.MediCare.model.entity.Paziente import Paziente

class MedicoService:

    @classmethod
    def getPazienti(cls,dottore):
        medico = Medico.query.filter_by(email=dottore).first()

        if medico:
            prenotazioni_medico = medico.prenotazioni
            codici_fiscali = [prenotazione.pazienteCF for prenotazione in prenotazioni_medico]
            pazienti = Paziente.query.filter(Paziente.CF.in_(codici_fiscali)).all()
            return pazienti
        else:
            return None






