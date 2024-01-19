import re

from flask import redirect, url_for, session
from flask_login import login_user, logout_user
from flaskDir import db, app, login
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.EnteFunction.EnteService import EnteService
from flaskDir.source.Medico.MedicoService import MedicoService
from flaskDir.source.Utente.PazienteService import PazienteService

medicoService = MedicoService()
pazienteService = PazienteService()
@login.user_loader
def load_user(id): #Bisogna aggiungere anche l'utente
    """
    Carica un utente dal database in base al suo ID.

    Args:
        id (str): L'ID dell'utente nel sistema.

    Returns:
        Utente: L'oggetto utente corrispondente all'ID fornito.
    """
    user_role = session['user_role']
    if user_role == 'paziente':
        return db.session.get(Paziente, id)

    elif user_role == 'medico':
        return db.session.get(Medico, id)
    elif user_role == 'ente':
        return db.session.get(EnteSanitario, id)

def login_page(email,password,tipo):
    """
        Gestisce il processo di login per medici e pazienti.

        Args:
            email (str): L'indirizzo email dell'utente.
            password (str): La password dell'utente.
            tipo (str): Il tipo di utente ('medico' o 'paziente').

        Returns:
            bool: True se il login ha avuto successo, False altrimenti.
    """
    formato_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not formato_email.match(email): return False
    if not 8 <= len(password) <= 255: return False


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
    """
    Gestisce il processo di login per gli enti sanitari.

    Args:
        email (str): L'indirizzo email dell'ente.
        password (str): La password dell'ente.

    Returns:
        bool: True se il login ha avuto successo, False altrimenti.
    """

    formato_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not formato_email.match(email): return False
    if not 8 <= len(password) <= 255: return False

    ente = EnteService.retrieveEnte(email, password)
    if ente is None:
        return False  # Gli potrei aggiungere la notifica che le credenziali son oerrate
    login_user(ente)  # Potremmo chidere anche se l'utente vuole essere ricordato
    session['user_role'] = 'ente'

    return True



def registrazione_pageMedico(email,password,nome,cognome,iscrizione,specializzazione,citta):
    """
        Registra un nuovo medico nel sistema.

        Args:
            email (str): L'indirizzo email del medico.
            password (str): La password del medico.
            nome (str): Il nome del medico.
            cognome (str): Il cognome del medico.
            iscrizione (str): Il numero di iscrizione dell'albo medico.
            specializzazione (str): La specializzazione del medico.
            citta (str): La città di residenza del medico.

        Returns:
            bool: True se la registrazione ha avuto successo, False altrimenti.
    """
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
    """
       Registra un nuovo paziente nel sistema.

       Args:
           email (str): L'indirizzo email del paziente.
           password (str): La password del paziente.
           nome (str): Il nome del paziente.
           cognome (str): Il cognome del paziente.
           CF (str): Il codice fiscale del paziente.
           cellulare (str): Il numero di cellulare del paziente.
           luogoNascita (str): Il luogo di nascita del paziente.
           domicilio (str): Il domicilio del paziente.
           dataNascita (str): La data di nascita del paziente (formato YYYY-MM-DD).
           sesso (str): Il genere del paziente ('M' o 'F').

       Returns:
           bool: True se la registrazione ha avuto successo, False altrimenti.
    """
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
    """
        Registra un nuovo ente sanitario nel sistema.

        Args:
            email (str): L'indirizzo email dell'ente.
            password (str): La password dell'ente.
            nome (str): Il nome dell'ente.
            citta (str): La città di ubicazione dell'ente.

        Returns:
            bool: True se la registrazione ha avuto successo, False altrimenti.
    """
    ente = EnteService.retrieveEnte(email, password)
    if ente is not None:
        return False
    ente = EnteSanitario()
    with app.app_context():
        ente.nome = nome
        ente.email = email
        ente.set_password(password)
        ente.città = citta
        db.session.add(ente)
        db.session.commit()
    return True


def logout():
    """
    Esegue il logout dell'utente corrente.

    Returns:
        redirect: Reindirizza l'utente alla pagina home dopo il logout.
    """
    logout_user()
    return redirect(url_for('home'))