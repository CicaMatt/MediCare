import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

from flaskDir import db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.MediCare.model.entity.Farmaco import Farmaco




class MedicoService:
    """

    """
    #Invece di fare operazioni di input output ad ogni richiesta, memorizzo listamedici
    _listaMedici = None

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

    def filtraMedici(cls, specializzazione = None, citta = None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        newList = []
        if specializzazione is not None and citta is not None:
            newList = [medico for medico in cls._listaMedici if medico.città == citta and medico.specializzazione == specializzazione]

        elif citta is not None:
            newList = [medico for medico in cls._listaMedici if medico.città == citta]

        elif specializzazione is not None:
            newList = [medico for medico in cls._listaMedici if medico.specializzazione == specializzazione]

        return newList

    def filtraMediciv2(cls, specializzazione = None, citta = None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        listaFiltrata = []
        condizioniDaVerificare = []

        if specializzazione is not None:
            condizioniDaVerificare.append(lambda medico: medico.specializzazione == specializzazione)
        if citta is not None:
            condizioniDaVerificare.append(lambda medico: medico.città == citta)

        listaFiltrata = [medico for medico in cls._listaMedici if all(condition(medico) for condition in condizioniDaVerificare)]

        return listaFiltrata

    @classmethod
    def addMedicotoLista(cls, medico):
        cls._listaMedici = cls.getListaMedici()
        cls._listaMedici.append(medico)


    @classmethod
    def rimuoviMedico(cls,email):
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

class PazienteService:

    @staticmethod
    def retrievePaziente(email, password):
        paziente = db.session.scalar(sqlalchemy.select(Paziente).where(Paziente.email == email))
        if paziente is None or not paziente.check_password(password):
            return None
        return paziente
    @classmethod
    def getListaVaccini(cls, user):
        return DocumentoSanitario.query.filter_by(titolare=user.CF, tipo="vaccino")

    @classmethod
    def getListaPrenotazioni(cls, user):
        return db.session.scalars(sqlalchemy.select(Prenotazione).where(Prenotazione.pazienteCF == user.CF))


    @classmethod
    def eliminaPaziente(cls, cf):
        try:
            Prenotazione.query.filter_by(pazienteCF=cf).delete()
            DocumentoSanitario.query.filter_by(titolare=cf).delete()
            MetodoPagamento.query.filter_by(beneficiaro=cf).delete()
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

class PrenotazioneService:

    @classmethod
    def getListaMedici(cls,specializzazione = None, citta= None):
        return MedicoService().filtraMedici(specializzazione,citta)
    @classmethod
    def getListaVaccini(cls,user):
        return PrenotazioneService.getListaVaccini(user)

    @classmethod
    def getListaPrenotazioni(cls, user):
        return PazienteService.getListaPrenotazioni(user)
    @classmethod
    def confirmIsFree(cls, idmedico, data, ora):
        prenotazioni = Prenotazione.query.filter_by(medico=idmedico, oraVisita=ora, dataVisita=data).first()
        if prenotazioni: #Se ci sono prenotazioni per quella data allora non è free
            return False
        return True

    @staticmethod
    def savePrenotazione (idmedico, data, ora, tipo, CF, prezzo):

        try:
            medico=MedicoService().getMedico(idmedico)

            prenotazione = Prenotazione()
            prenotazione.medico = idmedico
            prenotazione.pazienteCF = CF
            prenotazione.tipoVisita = tipo
            prenotazione.dataVisita = data
            prenotazione.oraVisita = ora
            prenotazione.prezzo = prezzo
            prenotazione.prenMed = medico


            db.session.add(prenotazione)

            db.session.commit()

        except SQLAlchemyError as e:
            print("Errore mentre salvavo la prenotazione: {}".format(e))

            db.session.rollback()

            return False




    @classmethod
    def modificaPrenotazione(cls, id, data, ora):
        try:
            prenotazioni = Prenotazione.query.filter_by(ID=id).first()
            if prenotazioni:
                prenotazioni.dataVisita = data
                prenotazioni.oraVisita = ora
                db.session.commit()

                return True
            else:
                return False

        except SQLAlchemyError as e:
            print("Errore mentre modificavo la prenotazione: {}".format(e))

            db.session.rollback()

            return False

class EnteService:
    @staticmethod
    def retrieveEnte(email, password):
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email))
        if ente is None or not ente.check_password(password):
            return None
        return ente



class FascicoloService:

    @classmethod
    def getDocumentiSanitari(cls, cf):
        return DocumentoSanitario.query.filter_by(titolare=cf)



class FarmaciService:

    @classmethod
    def getFarmaci(cls):
        return Farmaco.query.all()















