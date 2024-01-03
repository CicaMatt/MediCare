from flask import Blueprint, render_template, session, request
from flask_login import current_user

from flaskDir.source.prenotazioni.services import PrenotazioneService, FascicoloService

areautente_blueprint = Blueprint('areautente', __name__)

@areautente_blueprint.route('/storico')
def getPrenotazionibyUtente():
    return render_template("Storico.html")
    return render_template("Storico.html", lista=PrenotazioneService.getListaPrenotazioni(current_user))



@areautente_blueprint.route('/fascicolo')
def getFascicolobyUtente():
    CF=request.args.get('CF')
    return render_template("FascicoloElettronico.html",lista= FascicoloService.getDocumentiSanitari(CF))