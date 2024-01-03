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
    #quando l'area di login paziente sara' pronta invece di mettere il codice fiscale manualmente inseriremo quello preso dalla request
    #user=request.args.get("CF")
                                                                            #qua verra' inserito getDocumentiSanitari(CF)
    return render_template("FascicoloElettronico.html",lista= FascicoloService.getDocumentiSanitari("MRSRSS029DGH6712"))