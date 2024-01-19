from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required
import datetime
from flaskDir.source.Fascicolo.FascicoloService import FascicoloService
from flaskDir.source.Utente.PazienteService import PazienteService
from flaskDir.source.prenotazioni.PrenotazioneService import PrenotazioneService

areautente_blueprint = Blueprint('areautente', __name__)


@areautente_blueprint.route('/storico')
@login_required
def storico():
    """
    Restituisce la pagina dello storico delle prenotazioni per l'utente corrente.

    Returns:
    str: Pagina HTML dello storico delle prenotazioni.
    """
    return render_template("Storico.html", lista=PrenotazioneService.getListaPrenotazioni(current_user),
                           oggi=datetime.date.today())


@areautente_blueprint.route('/storicoMedico', methods=['GET', 'POST'])
@login_required
def getstoricoMedico():
    """
    Restituisce la pagina dello storico delle prenotazioni per un medico.

    Returns:
    str: Pagina HTML dello storico delle prenotazioni del medico.
    """
    medico = request.args.get('medico')
    return render_template("StoricoPrenotazioniMedico.html",
                           lista=PrenotazioneService.getListaPrenotazioniMedico(medico))


@areautente_blueprint.route('/fascicolo', methods=['GET', 'POST'])
@login_required
def getFascicolobyUtente(paziente=None):
    """
    Restituisce la pagina del fascicolo elettronico per l'utente corrente.

    Args:
    - paziente (str, optional): Il codice fiscale del paziente. Se non specificato, viene letto dalla richiesta.

    Returns:
    str: Pagina HTML del fascicolo elettronico.
    """
    if paziente is None:
        paziente = request.args.get('paziente')
    return render_template("FascicoloElettronico.html", listaDOC=FascicoloService.getDocumentiSanitari(paziente).all(),
                           cfPaziente=paziente)


@areautente_blueprint.route('/eliminapaziente', methods=['GET', 'POST'])
@login_required
def eliminaPaziente():
    """
    Elimina il paziente corrente.

    Returns:
    JSON: Risposta JSON che indica l'esito dell'operazione.
    """
    cf = current_user.CF
    if cf is None:
        return jsonify({"error": "Utente non trovato nella sessione"}), 400

    success = PazienteService.eliminaPaziente(cf)

    if success:
        return jsonify({"message": "Paziente eliminato con successo"})
    else:
        return jsonify({"error": "Errore durante l'eliminazione del paziente"}), 500


@areautente_blueprint.route('/addDocumento', methods=['GET', 'POST'])
@login_required
def addDocumento():
    """
    Aggiunge un documento al fascicolo elettronico.

    Returns:
    str: Redirect alla pagina del fascicolo elettronico.
    """
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        richiamo = None
        descrizione = request.form.get('descrizione')
        paziente = request.form.get('cf')
        if tipo == "Vaccino":
            richiamo = request.form.get('richiamo')
        FascicoloService.addDocumento(tipo, descrizione, richiamo, paziente)
    return redirect(url_for('areautente.getFascicolobyUtente', paziente=paziente))


@areautente_blueprint.route('/modificaPrenotazione', methods=['GET', 'POST'])
def modificaPrenotazione():
    """
    Modifica una prenotazione.

    Returns:
    str: Pagina HTML dello storico delle prenotazioni con il risultato dell'operazione.
    """
    if request.method == 'POST':
        data = request.form.get('data')
        ora = request.form.get('ora')
        id = request.form.get('id')
        if PrenotazioneService.modificaPrenotazione(id, data, ora):
            return render_template("Storico.html", lista=PazienteService.getListaPrenotazioni(current_user),
                                   messaggio=None, oggi=datetime.date.today())
        else:
            return render_template("Storico.html", lista=PazienteService.getListaPrenotazioni(current_user),
                                   messaggio="messaggio", oggi=datetime.date.today())
