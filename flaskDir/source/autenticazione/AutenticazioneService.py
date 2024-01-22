import re
import smtplib
from datetime import datetime

import pyotp

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
def load_user(cf):  # Bisogna aggiungere anche l'utente
    """
    Carica un utente dal database in base al suo ID.

    Args:
        cf (str): L'ID dell'utente nel sistema.

    Returns:
        Utente: L'oggetto utente corrispondente all'ID fornito.
    """
    user_role = session['user_role']
    if user_role == 'paziente':
        return db.session.get(Paziente, cf)

    elif user_role == 'medico':
        return db.session.get(Medico, cf)
    elif user_role == 'ente':
        return db.session.get(EnteSanitario, cf)


def login_page(email, password, tipo):
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
    if not formato_email.match(email):
        return False
    if not 8 <= len(password) <= 255:
        return False

    if tipo == 'medico':
        medico = medicoService.retrieveMedico(email, password)
        if medico is None:
            return False  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(medico)
        session['user_role'] = 'medico'
        return True

    else:
        paziente = pazienteService.retrievePaziente(email, password)
        if paziente is None:
            return False
        oggetto = "Subject: Codice di autenticazione di MediCare\n\n"
        codice = genera_token_totp(genera_codice_segreto())
        contenuto = "Hai provato ad accedere a MediCare il giorno " + datetime.now().strftime(
            "%d/%m/%Y %H:%M\n") + codice +("\n Se non sei stato tu prova a contattare l'assistenza di Medicare"
                                           "all'e-mail medicare.servizi@gmail.com")
        messaggio = oggetto + contenuto
        sessione = smtplib.SMTP("smtp-mail.outlook.com", 587)
        sessione.ehlo()
        sessione.starttls()
        sessione.login("giovannicasaburi02@gmail.com", "giovanni21")
        sessione.sendmail("giovannicasaburi02@gmail.com", email, messaggio)
        sessione.quit()
        session['2FA'] = codice
        session['user_role'] = "paziente"
        session['notActive'] = paziente.CF
        return True


def auth_2fa(codice_user):
    if session['2FA'] == codice_user:
        login_user(load_user(session.get('notActive')))
        session['2FA'] = None
        session['notActive'] = None
        return True
    else:
        session['2FA'] = None
        session['notActive'] = None
        session['user_role'] = None
        return False


def loginEnte_page(email, password):
    """
    Gestisce il processo di login per gli enti sanitari.

    Args:
        email (str): L'indirizzo email dell'ente.
        password (str): La password dell'ente.

    Returns:
        bool: True se il login ha avuto successo, False altrimenti.
    """

    formato_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not formato_email.match(email):
        return False
    if not 8 <= len(password) <= 255:
        return False

    ente = EnteService.retrieveEnte(email, password)
    if ente is None:
        return False  # Gli potrei aggiungere la notifica che le credenziali son oerrate
    login_user(ente)  # Potremmo chidere anche se l'utente vuole essere ricordato
    session['user_role'] = 'ente'

    return True


def registrazione_pageMedico(email, password, nome, cognome, iscrizione, specializzazione, citta):
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
    medico = Medico.query.filter_by(email=email).first()
    if medico is not None:
        return False
    medico = Medico()
    with app.app_context():
        medico.email = email
        medico.set_password(password)
        medico.nome = nome
        medico.cognome = cognome
        medico.iscrizione_albo = int(iscrizione)
        medico.specializzazione = specializzazione
        medico.tariffa = 50.00
        # noinspection NonAsciiCharacters
        medico.città = citta
        db.session.add(medico)
        db.session.commit()

        medicoService.addMedicotoLista(medico)

        return True


def registrazionePaziente(email, password, nome, cognome, CF, cellulare, luogoNascita, domicilio, dataNascita, sesso):
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
    paziente = Paziente.query.filter_by(email=email).first()
    if paziente:
        return False
    paziente = Paziente()
    with app.app_context():
        paziente.CF = CF
        paziente.chiaveSPID = 1
        paziente.email = email
        paziente.nome = nome
        paziente.cognome = cognome
        paziente.set_password(password)
        paziente.cellulare = cellulare
        paziente.domicilio = domicilio
        paziente.dataNascita = dataNascita
        paziente.luogoNascita = luogoNascita
        paziente.sesso = sesso

        db.session.add(paziente)
        db.session.commit()
        return True


def registrazioneEnte(email, password, nome, citta):
    """
    Registra un nuovo ente sanitario nel sistema.

    Args:
        email (str): L'indirizzo email dell'ente.
        password (str): La password dell'ente.
        nome (str): Il nome dell'ente.
        citta (str): La città di ubicazione dell'ente.

        Returns:
        bool: True se la registrazione ha avuto successo, False altrimenti.
        :param email:
        :param nome:
        :param password:
        :param citta:
    """
    ente = EnteSanitario.query.filter_by(email=email).first()
    if ente is not None:
        return False
    ente = EnteSanitario()
    with app.app_context():
        ente.nome = nome
        ente.email = email
        ente.set_password(password)
        # noinspection NonAsciiCharacters
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


# GENERAZIONE QR E 2FA
def genera_codice_segreto():
    segreto = pyotp.random_base32()
    return segreto


def genera_token_totp(segreto):
    totp = pyotp.TOTP(segreto)
    token = totp.now()
    return token


def verifica_token_totp(segreto, token):
    totp = pyotp.TOTP(segreto)
    return totp.verify(token)
