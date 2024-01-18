import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import datetime
from flaskDir import db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.source.Medico.MedicoService import MedicoService
from flaskDir.source.Utente.PazienteService import PazienteService


class PrenotazioneService:

    @classmethod
    def getListaMedici(cls,specializzazione = None, citta= None):
        return MedicoService().filtraMedici(specializzazione,citta)

    @classmethod
    def getListaVaccini(cls,user):
        return PazienteService.getListaVaccini(user)

    @classmethod
    def getListaPrenotazioni(cls, user):
        return PazienteService.getListaPrenotazioni(user)

    @classmethod
    def getListaPrenotazioniMedico(cls, medico):
        medico=Medico.query.filter(Medico.email==medico).first()
        if medico.ente_sanitario is None:
            return db.session.scalars(sqlalchemy.select(Prenotazione).where(Prenotazione.medico == medico.email))
        else:
            return db.session.scalars(sqlalchemy.select(Prenotazione).where(Prenotazione.medico == medico.email or Prenotazione.medico == medico.ente_sanitario))

    @classmethod
    def confirmIsFree(cls, idmedico, data, ora):
        mese=datetime.datetime.now().strftime("%m")+"-"
        if int(data) <= datetime.datetime.now().day:
            mese = str(datetime.datetime.now().month + 1)
            mese = mese + "-"
        anno=datetime.datetime.now().strftime("%Y")+"-"
        data=str(anno)+str(mese)+str(data)
        prenotazioni = Prenotazione.query.filter_by(medico=idmedico, oraVisita=ora, dataVisita=data).first()
        if prenotazioni: #Se ci sono prenotazioni per quella data allora non è free
            return False
        return True

    @staticmethod
    def savePrenotazione (idmedico, data, ora, tipo, CF, prezzo, carta="SSS"):

        try:
            medico=MedicoService().getMedico(idmedico)
            mese = datetime.datetime.now().strftime("%m") + "-"

            if int(data)<=datetime.datetime.now().day:
                mese = str(datetime.datetime.now().month+1)
                mese=mese+"-"
            anno = datetime.datetime.now().strftime("%Y") + "-"
            data = str(anno) + str(mese) + str(data)
            prenotazione = Prenotazione()
            prenotazione.medico = idmedico
            prenotazione.pazienteCF = CF
            prenotazione.tipoVisita = tipo
            prenotazione.dataVisita = data
            if  8<=int(ora)<=19:
                prenotazione.oraVisita = int(ora)
            else: raise SQLAlchemyError
            if float(prezzo)<=0:
                raise SQLAlchemyError
            prenotazione.prezzo = float(prezzo)
            prenotazione.prenMed = medico
            if carta.isdigit():
                prenotazione.pagata = True


            db.session.add(prenotazione)

            db.session.commit()

        except SQLAlchemyError as e:
            print("Errore mentre salvavo la prenotazione: {}".format(e))

            db.session.rollback()

            return False
    @staticmethod
    def saveVaccino(idmedico, data, ora, tipo, CF, prezzo=0):

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
            if prenotazioni and PrenotazioneService.confirmIsFree(prenotazioni.medico,data, ora):
                mese = datetime.datetime.now().strftime("%m") + "-"
                if int(data)<=datetime.datetime.now().day:
                    mese = str(datetime.datetime.now().month + 1)
                    mese = mese + "-"
                anno = datetime.datetime.now().strftime("%Y") + "-"
                data = str(anno) + str(mese) + str(data)
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

    @classmethod
    def getGiorniCorrenti(cls):
        # Ottenere la data corrente
        oggi = datetime.datetime.now()

        # Ottenere l'anno e il mese corrente
        anno_corrente = oggi.year
        mese_corrente = oggi.month

        # Calcolare il primo giorno del mese corrente
        primo_giorno_mese = datetime.datetime(anno_corrente, mese_corrente, 1)

        # Calcolare il numero di giorni rimanenti nel mese corrente
        giorni_passati = oggi.day  # Giorni già passati nel mese corrente

        # Calcolare il primo giorno del mese successivo
        primo_giorno_mese_successivo = datetime.datetime(anno_corrente, mese_corrente + 1,
                                                         1) if mese_corrente < 12 else datetime.datetime(
            anno_corrente + 1, 1, 1)
        ultimo_giorno_mese_corrente = primo_giorno_mese_successivo - datetime.timedelta(days=1)

        # Calcolare il numero di giorni nel mese corrente
        numero_giorni_mese_corrente = (ultimo_giorno_mese_corrente - primo_giorno_mese).days + 1

        # Calcolare il numero di giorni nel mese successivo
        giorni_mese_successivo = giorni_passati

        return numero_giorni_mese_corrente, giorni_mese_successivo

    @classmethod
    def confirmVaccino(cls, idmedico, data, ora):
        prenotazioni = Prenotazione.query.filter_by(medico=idmedico, oraVisita=ora, dataVisita=data).first()
        if prenotazioni:  # Se ci sono prenotazioni per quella data allora non è free
            return False
        return True