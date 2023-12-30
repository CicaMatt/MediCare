from flask import render_template, session, request, Blueprint

from flaskDir import app
from flaskDir.MediCare.model.entity import Medici
from flaskDir.source.prenotazioni import MedicoControl
from flaskDir.source.prenotazioni.services import PrenotazioneService, MedicoService

# Dovrebbe essere un singleton?!

# Creo una "mappa" (blueprint) che definisce tante strade (routes), poi in app.py registro anche questa mappa
prenotazione_blueprint = Blueprint('prenotazioni', __name__)


@prenotazione_blueprint.route('/listamedici')
def getListaMedici():
    specializzazione = request.args.get('specializzazione')
    citta = request.args.get('citta')
    # Se usiamo la get request.args.get['']
    return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici(specializzazione, citta))


@prenotazione_blueprint.route('/listamedici/paginamedico', methods=['POST'])
def getMedico():
    idMedico = request.form['medico']
    if idMedico == None:
        return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici())


    data = request.form['data']
    ora = request.form['ora']
    medico = MedicoService.getMedico(idMedico)

    #Se ha scelto la data e l'ora
    if data and ora and 'user' in session:
        user = session['user']
        if PrenotazioneService.checkIfFree(data, ora):
            PrenotazioneService.savePrenotazione(data, ora, medico, user)
    # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
    else:
        return render_template("PaginaMedico.html", medico=medico)


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