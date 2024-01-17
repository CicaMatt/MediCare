
from flask import render_template, session, request, Blueprint
from flask_login import current_user, login_required

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
    richiamo=request.args.get('richiamo')
    return render_template("ListaEnti.html", lista=MedicoService.getListaCentri(), richiamo=richiamo)


@prenotazione_blueprint.route('/listamedici/paginamedico', methods=['GET','POST'])
@login_required
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
    prezzo=float(medico.tariffa)

    #Dopo che ha scelto la data e l'ora
    if data and ora and current_user.is_authenticated:


        if PrenotazioneService.confirmIsFree(idMedico,data, ora):

            if paziente.ISEE_ordinario is not None and paziente.ISEE_ordinario <=10000:
                prezzo=prezzo-(prezzo*33)/100
            elif paziente.ISEE_ordinario is not None and paziente.ISEE_ordinario <=20000:
                prezzo=prezzo-(prezzo*10)/100

            PrenotazioneService.savePrenotazione(idMedico,data, ora,medico.specializzazione, user,prezzo,carta)
            #Pagina Prenotazione??
            return render_template("HomePage.html", medico=medico)
        else:
            return render_template("ProfiloMedico.html", medico=medico, alert="error", message="Impossibile salvare la prenotazione: data occupata", data=data, giorni=giorni, carte=paziente.carte, prezzo=prezzo)

    # Era meglio usare l'id come identificativo, adesso invece ogni utente può vedere la mail ei medici
    else:
        return render_template("ProfiloMedico.html", medico=medico, data=current_date, giorni=giorni, carte=paziente.carte, prezzo=prezzo)


@prenotazione_blueprint.route('/prenotazione/listavaccini')
def getListaVaccini():
    if '_user_id' in session:
        user = Paziente.query.filter(Paziente.CF==session.get('_user_id')).first()
        return render_template("Vaccini.html", lista=PrenotazioneService.getListaVaccini(user))
    return render_template("Prenotazione.html")

@prenotazione_blueprint.route('/saveVaccino', methods=['POST'])
def saveVaccino():
    if '_user_id' in session and request.method == 'POST':
        user = session['_user_id']
        medico=request.form['medico']
        richiamo=request.form['richiamo']
        if PrenotazioneService.confirmVaccino(medico,richiamo,11):
            PrenotazioneService.saveVaccino(medico,richiamo,11,"Vaccino",user)
            return render_template("HomePage.html")
        else: return render_template("ListaEnti.html", lista=MedicoService.getListaCentri(), richiamo=richiamo)





