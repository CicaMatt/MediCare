from flask import render_template, session, request, Blueprint
from flask_login import current_user, login_required

from flaskDir.MediCare.model.entity.Paziente import Paziente, paziente_required

from datetime import datetime

from flaskDir.source.Medico.MedicoService import MedicoService
from flaskDir.source.prenotazioni.PrenotazioneService import PrenotazioneService

# Dovrebbe essere un singleton?!

# Creo una "mappa" (blueprint) che definisce tante strade (routes), poi in app.py registro anche questa mappa
prenotazione_blueprint = Blueprint('prenotazioni', __name__)


@prenotazione_blueprint.route('/listamedici')
def getListaMedici():
    """
    Restituisce la lista dei medici disponibili.

    Returns:
        render_template: Template HTML con la lista dei medici.
    """
    specializzazione = request.args.get('specializzazione')
    citta = request.args.get('citta')
    # Se usiamo la get request.args.get['']
    return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici(specializzazione, citta))


@prenotazione_blueprint.route('/listaenti')
def getListaEnti():
    """
    Restituisce la lista degli enti disponibili.

    Returns:
        render_template: Template HTML con la lista degli enti.
    """
    richiamo = request.args.get('richiamo')
    return render_template("ListaEnti.html", lista=MedicoService.getListaCentri(), richiamo=richiamo)


@prenotazione_blueprint.route('/listamedici/paginamedico', methods=['GET', 'POST'])
@login_required
@paziente_required
def getMedico():
    """
    Restituisce le informazioni relative a un medico selezionato.

    Returns:
        render_template: Template HTML con le informazioni del medico.
    """
    idMedico = request.form.get('medico')
    user = session['_user_id']
    paziente = Paziente.query.filter(Paziente.CF == user).first()
    if idMedico is None:
        return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici())

    current_date = datetime.now().strftime("%B %Y")
    current_day = datetime.now().day + 1
    day_of_week = datetime.now().weekday() + 1
    giorni_rim, giorni_succ, partenza = PrenotazioneService.getGiorniCorrenti()
    data = request.form.get('giorno')
    ora = request.form.get('ora')
    carta = request.form.get('carta')
    medico = MedicoService.getMedico(idMedico)
    prezzo = float(medico.tariffa)
    prenotazioniMedico = PrenotazioneService.getListaPrenotazioniMedico(idMedico)
    orariOccupati = list((prenotazione.oraVisita, prenotazione.dataVisita) for prenotazione in prenotazioniMedico)

    # Dopo che ha scelto la data e l'ora
    if data and ora and current_user.is_authenticated:

        if PrenotazioneService.confirmIsFree(idMedico, data, ora):

            if paziente.ISEE_ordinario is not None and paziente.ISEE_ordinario <= 10000:
                prezzo = prezzo - (prezzo * 33) / 100
            elif paziente.ISEE_ordinario is not None and paziente.ISEE_ordinario <= 20000:
                prezzo = prezzo - (prezzo * 10) / 100

            PrenotazioneService.savePrenotazione(idMedico, data, ora, medico.specializzazione, user, prezzo, carta)
            # Pagina Prenotazione??
            return render_template("HomePage.html", medico=medico)
        else:
            return render_template("ProfiloMedico.html", medico=medico, alert="error",
                                   message="Impossibile salvare la prenotazione: data occupata", data=current_date,
                                   giorni=(giorni_rim, giorni_succ, partenza), carte=paziente.carte, prezzo=prezzo,
                                   day=current_day, week_day=day_of_week)

    # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
    else:
        return render_template("ProfiloMedico.html", medico=medico, data=current_date,
                               giorni=(giorni_rim, giorni_succ, partenza), carte=paziente.carte, prezzo=prezzo,
                               day=current_day,
                               week_day=day_of_week, orariOccupati=orariOccupati)


@prenotazione_blueprint.route('/prenotazione/listavaccini')
@paziente_required
def getListaVaccini():
    """
    Restituisce la lista dei vaccini disponibili.

    Returns:
        render_template: Template HTML con la lista dei vaccini.
    """
    if '_user_id' in session:
        user = Paziente.query.filter(Paziente.CF == session.get('_user_id')).first()
        return render_template("Vaccini.html", lista=PrenotazioneService.getListaVaccini(user))
    return render_template("Prenotazione.html")


@prenotazione_blueprint.route('/saveVaccino', methods=['POST'])
def saveVaccino():
    """
    Salva un vaccino per un paziente.

    Returns:
        render_template: Template HTML per la homepage.
    """
    if '_user_id' in session and request.method == 'POST':
        user = session['_user_id']
        medico = request.form['medico']
        richiamo = request.form['richiamo']
        if PrenotazioneService.confirmVaccino(medico, richiamo, 11):
            PrenotazioneService.saveVaccino(medico, richiamo, 11, "Vaccino", user)
            return render_template("HomePage.html")
        else:
            return render_template("ListaEnti.html", lista=MedicoService.getListaCentri(), richiamo=richiamo)
