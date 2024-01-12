
from flask import render_template, session, request, Blueprint
from flask_login import current_user

from flaskDir import app
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.prenotazioni.services import PrenotazioneService, MedicoService
from datetime import datetime

# Dovrebbe essere un singleton?!

# Creo una "mappa" (blueprint) che definisce tante strade (routes), poi in app.py registro anche questa mappa
prenotazione_blueprint = Blueprint('prenotazioni', __name__)


@prenotazione_blueprint.route('/listamedici')
def getListaMedici():
    specializzazione = request.args.get('specializzazione')
    citta = request.args.get('citta')
    # Se usiamo la get request.args.get['']
    return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici(specializzazione, citta))


@prenotazione_blueprint.route('/listaenti')
def getListaEnti():
    return render_template("ListaEnti.html", lista=MedicoService.getListaEnti())


@prenotazione_blueprint.route('/listamedici/paginamedico', methods=['GET','POST'])
def getMedico():
    idMedico = request.form.get('medico')
    user = session['_user_id']
    paziente=Paziente.query.filter(Paziente.CF==user).first()
    if idMedico == None:
        return render_template("ListaMedici.html", lista=PrenotazioneService.getListaMedici())

    current_date=datetime.now().strftime("%B %Y")
    giorni=PrenotazioneService.getGiorniCorrenti()
    data = request.form.get('giorno')
    ora = request.form.get('ora')
    carta=request.form.get('carta')
    medico = MedicoService.getMedico(idMedico)

    #Dopo che ha scelto la data e l'ora
    if data and ora and current_user.is_authenticated:


        if PrenotazioneService.confirmIsFree(idMedico,data, ora):

            PrenotazioneService.savePrenotazione(idMedico,data, ora,medico.specializzazione, user,50,carta)
            #Pagina Prenotazione??
            return render_template("HomePage.html", medico=medico)
        else:
            return render_template("ProfiloMedico.html", medico=medico, alert="error", message="Impossibile salvare la prenotazione: data occupata", data=data, giorni=giorni, carte=Paziente.carte)

    # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
    else:
        return render_template("ProfiloMedico.html", medico=medico, data=current_date, giorni=giorni, carte=paziente.carte)


@app.route('/prenotazione/listavaccini')
def getListaVaccini():
    if 'user' in session:
        user = session['user']
        return render_template("Vaccini.html", lista=PrenotazioneService.getListaVaccini(user))
    return render_template("Prenotazione.html")





