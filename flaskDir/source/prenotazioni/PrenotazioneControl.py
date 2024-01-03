
from flask import render_template, session, request, Blueprint
from flask_login import current_user

from flaskDir import app
from flaskDir.MediCare.model.entity import Medici
from flaskDir.source.prenotazioni import MedicoControl
from flaskDir.source.prenotazioni.services import PrenotazioneService, MedicoService
from datetime import datetime

# Dovrebbe essere un singleton?!

# Creo una "mappa" (blueprint) che definisce tante strade (routes), poi in app.py registro anche questa mappa
prenotazione_blueprint = Blueprint('prenotazioni', __name__)


@prenotazione_blueprint.route('/listamedici')
def getListaMedici():
    specializzazione = request.args.get('specializzazione')
    citta = request.args.get('citta')
    # Se usiamo la get request.args.get['']
    return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici(specializzazione, citta))


@prenotazione_blueprint.route('/listamedici/paginamedico', methods=['GET','POST'])
def getMedico():
    idMedico = request.form.get('medico')
    if idMedico == None:
        return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici())

    current_date=datetime.now().strftime("%B %Y")
    data = request.form.get('data')
    ora = request.form.get('ora')
    medico = MedicoService.getMedico(idMedico)

    #Dopo che ha scelto la data e l'ora
    if data and ora and current_user.is_authenticated:
        user = session['user']
        if PrenotazioneService.confirmIsFree(data, ora):
            PrenotazioneService.savePrenotazione(data, ora, medico, user)
            #Pagina Prenotazione??
            return render_template("ProfiloMedico.html", medico=medico)
        else:
            return render_template("ProfiloMedico.html", medico=medico, alert="error", message="Impossibile salvare la prenotazione: data occupata")

    # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
    else:
        return render_template("ProfiloMedico.html", medico=medico, data=current_date)


@app.route('/prenotazione/listavaccini')
def getListaVaccini():
    if 'user' in session:
        user = session['user']
        return render_template("Vaccini.html", lista=PrenotazioneService.getListaVaccini(user))
    return render_template("Prenotazione.html")


"""
from flask import render_template, request
from flaskDir import app
from flaskDir.MediCare.model.entity import Medici
from flaskDir.source.prenotazioni import MedicoControl
from flaskDir.source.prenotazioni.services import PrenotazioneService

class PrenotazioneControl:
    _prService = PrenotazioneService()

    @staticmethod
    @app.route('/prenotazione/listamedici', methods=['GET'])
    def getListaMedici(cls):
        specializzazione = request.args.get('specializzazione')
        citta = request.args.get('citta')
        return render_template("ListaMedici.html", lista=PrenotazioneControl._prService.getListaMedici())

    @staticmethod
    @app.route('/prenotazione/listamedici/<medico>', methods=['GET'])
    def getMedico(cls, medico=None):
        mailMedico = request.args.get('medico')
        return render_template("PaginaMedico.html", medico=mailMedico)

    @staticmethod
    @app.route('/prenotazione/listavaccini', methods=['GET'])
    def getListaVaccini(cls):
        user = request.args.get('user')  # Assicurati di passare 'user' come parametro o dal client
        return render_template("Vaccini.html", lista=PrenotazioneControl._prService.getListaVaccini(user))

"""
