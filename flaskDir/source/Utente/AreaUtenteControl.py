from flask import Blueprint, render_template, session, request, redirect, url_for, jsonify
from flask_login import current_user, login_required
import datetime
from flaskDir.source.prenotazioni import services
from flaskDir.source.prenotazioni.services import PrenotazioneService, FascicoloService, PazienteService

areautente_blueprint = Blueprint('areautente', __name__)

@areautente_blueprint.route('/storico')
@login_required
def storico():
    return render_template("Storico.html", lista=PrenotazioneService.getListaPrenotazioni(current_user), oggi=datetime.date.today())

@areautente_blueprint.route('/storicoMedico',methods=['GET','POST'])
@login_required
def getstoricoMedico():
    medico = request.args.get('medico')
    return render_template("StoricoPrenotazioniMedico.html", lista=PrenotazioneService.getListaPrenotazioniMedico(medico))



@areautente_blueprint.route('/fascicolo',methods=['GET','POST'])
@login_required
def getFascicolobyUtente(paziente=None):
    if paziente is None:
        paziente = request.args.get('paziente')
    return render_template("FascicoloElettronico.html",listaDOC= FascicoloService.getDocumentiSanitari(paziente).all(),cfPaziente=paziente)


@areautente_blueprint.route('/eliminapaziente',methods=['GET','POST'])
@login_required
def eliminaPaziente():
    cf = current_user.CF
    if cf is None:
        return jsonify({"error": "Utente non trovato nella sessione"}), 400

    success = services.PazienteService.eliminaPaziente(cf)

    if success:
        return jsonify({"message": "Paziente eliminato con successo"})
    else:
        return jsonify({"error": "Errore durante l'eliminazione del paziente"}), 500

@areautente_blueprint.route('/addDocumento',methods=['GET','POST'])
@login_required
def addDocumento():
    if request.method == 'POST':
        tipo=request.form.get('tipo')
        richiamo=None
        descrizione = request.form.get('descrizione')
        paziente = request.form.get('cf')
        if tipo == "Vaccino":
            richiamo=request.form.get('richiamo')
        FascicoloService.addDocumento(tipo,descrizione,richiamo,paziente)
    return redirect(url_for('areautente.getFascicolobyUtente', paziente=paziente))



@areautente_blueprint.route('/modificaPrenotazione', methods=['GET','POST'])
def modificaPrenotazione():
    if request.method == 'POST':
        data=request.form.get('data')
        ora=request.form.get('ora')
        id=request.form.get('id')
        if PrenotazioneService.modificaPrenotazione(id, data, ora):
            return render_template("Storico.html", lista=PazienteService.getListaPrenotazioni(current_user), messaggio=None)
        else:
            return render_template("Storico.html", lista=PazienteService.getListaPrenotazioni(current_user), messaggio="messaggio")
