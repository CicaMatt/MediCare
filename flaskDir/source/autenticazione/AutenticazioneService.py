from flask import redirect, url_for, render_template, session
from flask_login import current_user, login_user, logout_user
import sqlalchemy
from flaskDir import db, app, login
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.prenotazioni.services import MedicoService, PazienteService
from flaskDir.source.EnteFunction.EnteService import EnteService

medicoService = MedicoService()
pazienteService = PazienteService()
@login.user_loader
def load_user(id): #Bisogna aggiungere anche l'utente
    user_role = session['user_role']
    if user_role == 'paziente':
        return db.session.get(Paziente, id)

    elif user_role == 'medico':
        return db.session.get(Medico, id)
    elif user_role == 'ente':
        return db.session.get(EnteSanitario, id)

def login_page(email,password,tipo):
    if tipo =='medico':
        medico = medicoService.retrieveMedico(email, password)
        if medico == None:
            return False # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(medico)
        session['user_role'] = 'medico'
        return True

    else:
        paziente = pazienteService.retrievePaziente(email, password)
        if paziente == None:
            return False
        login_user(paziente)
        session['user_role'] = 'paziente'
        return True



def loginEnte_page(email,password):
    ente = EnteService.retrieveEnte(email, password)
    if ente is None:
        return False  # Gli potrei aggiungere la notifica che le credenziali son oerrate
    login_user(ente)  # Potremmo chidere anche se l'utente vuole essere ricordato
    session['user_role'] = 'ente'

    return True



def registrazione_pageMedico(email,password,nome,cognome,iscrizione,specializzazione,citta):
    medico=medicoService.retrieveMedico(email,password)
    if medico is not None:
        return False
    medico=Medico()
    with app.app_context():
        medico.email=email
        medico.set_password(password)
        medico.nome=nome
        medico.cognome=cognome
        medico.iscrizione_albo=int(iscrizione)
        medico.specializzazione=specializzazione
        medico.tariffa=50.00
        medico.città=citta
        db.session.add(medico)
        db.session.commit()

        medicoService.addMedicotoLista(medico)

        return True


def registrazionePaziente(email,password,nome,cognome,CF,cellulare,luogoNascita,domicilio,dataNascita,sesso):

    paziente=PazienteService.retrievePaziente(email,password)
    if paziente:
        return False
    paziente=Paziente()
    with app.app_context():
        paziente.CF=CF
        paziente.chiaveSPID=1
        paziente.email=email
        paziente.nome=nome
        paziente.cognome=cognome
        paziente.set_password(password)
        paziente.cellulare=cellulare
        paziente.domicilio=domicilio
        paziente.dataNascita=dataNascita
        paziente.luogoNascita=luogoNascita
        paziente.sesso=sesso

        db.session.add(paziente)
        db.session.commit()
        return True



def registrazioneEnte(email,password,nome,citta):

        ente=EnteService.retrieveEnte(email,password)
        if ente is not None:
            return False
        ente=EnteSanitario()
        with app.app_context():
            ente.nome=nome
            ente.email=email
            ente.set_password(password)
            ente.città=citta
            db.session.add(ente)
            db.session.commit()
        return True


def logout():
    logout_user()
    return redirect(url_for('home'))