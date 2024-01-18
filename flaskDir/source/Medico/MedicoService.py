import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente

class MedicoService:
    _listaMedici = None
    _listaCentri = None

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

    @staticmethod
    def getMedico(idMedico):
        return Medico.query.filter_by(email=idMedico).first()

    @staticmethod
    def retrieveMedico(email, password):
        medico = db.session.scalar(sqlalchemy.select(Medico).where(Medico.email == email))
        if medico is None or not medico.check_password(password):
            return None
        return medico

    @classmethod
    def getListaMedici(cls):
        if cls._listaMedici is None:
            cls._listaMedici = Medico.query.all()
        return cls._listaMedici

    @classmethod
    def getListaCentri(cls):
        if cls._listaCentri is None:
            cls._listaCentri = Medico.query.filter(Medico.specializzazione == "Vaccini").all()
        return cls._listaCentri

    def filtraMedici(cls, specializzazione=None, citta=None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        newList = []
        if specializzazione is not None and citta is not None:
            newList = [medico for medico in cls._listaMedici if
                       medico.città == citta and medico.specializzazione == specializzazione]

        elif citta is not None:
            newList = [medico for medico in cls._listaMedici if medico.città == citta]

        elif specializzazione is not None:
            newList = [medico for medico in cls._listaMedici if medico.specializzazione == specializzazione]

        return newList

    def filtraMediciv2(cls, specializzazione=None, citta=None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        listaFiltrata = []
        condizioniDaVerificare = []

        if specializzazione is not None:
            condizioniDaVerificare.append(lambda medico: medico.specializzazione == specializzazione)
        if citta is not None:
            condizioniDaVerificare.append(lambda medico: medico.città == citta)

        listaFiltrata = [medico for medico in cls._listaMedici if
                         all(condition(medico) for condition in condizioniDaVerificare)]

        return listaFiltrata

    @classmethod
    def addMedicotoLista(cls, medico):
        cls._listaMedici = cls.getListaMedici()
        cls._listaMedici.append(medico)

    @classmethod
    def rimuoviMedico(cls, email):
        try:
            medico = Medico.query.filter_by(email=email).first()
            if medico:
                db.session.delete(medico)
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            print("Errore durante l'eliminazione del medico: {}".format(e))
            # Rollback in caso di errore
            db.session.rollback()
            return False






