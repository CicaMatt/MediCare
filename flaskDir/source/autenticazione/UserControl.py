from urllib.parse import urlsplit

from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user
from flaskDir.source.autenticazione import AutenticazioneService

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login_page():
    """
    Gestisce la pagina di login.

    Returns:
        render_template: La pagina di login o la home se l'utente è già autenticato.
        redirect: Reindirizza l'utente alla home dopo il login con successo.
    """
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        tipo = request.form.get('tipo')
        next_page = request.args.get('next')
        if AutenticazioneService.login_page(email, password, tipo):
            if tipo != "paziente":
                if not next_page or urlsplit(next_page).netloc != '':
                    next_page = url_for('home')
                return redirect(next_page)
            else:
                return redirect(url_for('auth.verification2fa', next=next_page))
        else:
            return render_template('Login.html', error=False)
    else:
        return render_template('Login.html')


@auth_blueprint.route('/verification2fa', methods=['GET', 'POST'])
def verification2fa():
    if request.method == 'POST':
        codice = request.form.get('codice')
        if AutenticazioneService.auth_2fa(codice):
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
        else:
            return render_template('Login.html', error=False)
    else:
        return render_template('CodicePaziente.html')


@auth_blueprint.route('/loginente', methods=['GET', 'POST'])
def loginEnte_page():
    """
    Gestisce la pagina di login per gli enti sanitari.

    Returns:
        render_template: La pagina di login per gli enti o la home se l'utente è già autenticato.
        render_template: La home se il login dell'ente sanitario ha successo.
    """
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if AutenticazioneService.loginEnte_page(email, password):
            return render_template('HomePage.html')
    else:
        return render_template('LoginEnte.html')


@auth_blueprint.route('/registrazioneMedico', methods=['GET', 'POST'])
def registrazioneMedico():
    """
    Gestisce la registrazione di un nuovo medico.

    Returns:
        render_template: La pagina di registrazione del medico o la home se l'utente è già autenticato.
        render_template: La pagina di login se la registrazione del medico ha successo.
    """
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        iscrizione_albo = request.form.get('code')
        specializzazione = request.form.get('specializzazione')
        citta = request.form.get('citta')
        if AutenticazioneService.registrazione_pageMedico(email, password, nome, cognome, iscrizione_albo,
                                                          specializzazione, citta):
            return render_template('Login.html')
        else:
            return render_template('RegistrazioneMedico.html')


@auth_blueprint.route('/registrazionePaziente', methods=['GET', 'POST'])
def registrazionePaziente():
    """
    Gestisce la registrazione di un nuovo paziente.

    Returns:
        render_template: La pagina di registrazione del paziente o la home se l'utente è già autenticato.
        render_template: La home se la registrazione del paziente ha successo.
    """
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        CF = request.form.get('code')
        cellulare = request.form.get('cellulare')
        luogoNascita = request.form.get('cittanascita')
        domicilio = request.form.get('domicilio')
        dataNascita = request.form.get('datanascita')
        sesso = request.form.get('sesso')
        if AutenticazioneService.registrazionePaziente(email, password, nome, cognome, CF, cellulare, luogoNascita,
                                                       domicilio, dataNascita, sesso):
            return render_template('HomePage.html')
        else:
            return render_template('RegistrazionePaziente.html')


@auth_blueprint.route('/registrazione/ente', methods=['GET', 'POST'])
def registrazioneEnte():
    """
    Gestisce la registrazione di un nuovo ente sanitario.

    Returns:
        render_template: La pagina di registrazione dell'ente o la home se l'utente è già autenticato.
        render_template: La home se la registrazione dell'ente sanitario ha successo.
    """
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        password = request.form.get('password')
        citta = request.form.get('citta')
        if AutenticazioneService.registrazioneEnte(email, password, nome, citta):
            return render_template('HomePage.html')
        else:
            return render_template('RegistrazioneEnte.html')


@auth_blueprint.route('/logout')
def logout():
    """
    Esegue il logout dell'utente corrente.

    Returns:
        redirect: Reindirizza l'utente alla home dopo il logout.
    """
    return AutenticazioneService.logout()
