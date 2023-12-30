from flask import render_template, session, request

from flaskDir import app
from flaskDir.MediCare.model.entity import Medici
from flaskDir.source.prenotazioni import MedicoControl
from flaskDir.source.prenotazioni.services import PrenotazioneService


# Dovrebbe essere un singleton?!
class PrenotazioneControl:
    _prService = PrenotazioneService

    @app.route('/prenotazione/listamedici')
    def getListaMedici(cls):
        specializzazione = request.form['specializzazione']
        citta = request.form['citta']
        # Se usiamo la get request.args.get['']
        return render_template("ListaMedici.html", lista=cls._prService.getListaMedici())

    @app.route('/prenotazione/listamedici/<medico>')
    def getMedico(cls, medico=None):
        mailMedico = request.form[
            'medico']  # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
        return render_template("PaginaMedico.html", medico=mailMedico)

    @app.route('/prenotazione/listavaccini')
    @classmethod
    def getListaVaccini(cls):
        user = session['user']
        return render_template("Vaccini.html", lista=cls._prService.getListaVaccini(user))



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