from flask import Blueprint, render_template, session, request
from flask_login import current_user, login_required

from flaskDir.source.prenotazioni.services import PrenotazioneService, FascicoloService

areautente_blueprint = Blueprint('areautente', __name__)

@areautente_blueprint.route('/storico')
@login_required
def storico():

    return render_template("Storico.html", lista=PrenotazioneService.getListaPrenotazioni(current_user))



@areautente_blueprint.route('/fascicolo')
@login_required
def getFascicolobyUtente():
    CF=request.args.get('CF')
    #bisogna prendere il cf del paziente dalla sessione
    return render_template("FascicoloElettronico.html",lista= FascicoloService.getDocumentiSanitari(CF))