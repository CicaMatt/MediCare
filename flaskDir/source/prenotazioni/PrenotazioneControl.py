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
