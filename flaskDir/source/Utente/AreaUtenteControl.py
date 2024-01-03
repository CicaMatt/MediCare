from flask import Blueprint, render_template
from flask_login import current_user

from flaskDir.source.prenotazioni.services import PrenotazioneService

areautente_blueprint = Blueprint('areautente', __name__)

@areautente_blueprint.route('/storico')
def getPrenotazionibyUtente():
    return render_template("Storico.html")
    return render_template("Storico.html", lista=PrenotazioneService.getListaPrenotazioni(current_user))