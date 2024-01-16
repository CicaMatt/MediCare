from flask import Blueprint, request, render_template
from flask_login import current_user
from flaskDir.source.autenticazione import AutenticazioneService

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET','POST'])
def login_page():
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        tipo=request.form.get('tipo')
        if AutenticazioneService.login_page(email,password,tipo):
            return render_template('HomePage.html')
        else: return render_template('Login.html',error=False)
    else: return render_template('Login.html')


@auth_blueprint.route('/loginente', methods=['GET','POST'])
def loginEnte_page():
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        if AutenticazioneService.loginEnte_page(email, password):
            return render_template('HomePage.html')
    else: return render_template('LoginEnte.html')


@auth_blueprint.route('/registrazioneMedico', methods=['GET','POST'])
def registrazioneMedico():
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        iscrizione_albo = request.form.get('code')
        specializzazione = request.form.get('specializzazione')
        citta=request.form.get('citta')
        if AutenticazioneService.registrazione_pageMedico(email,password,nome,cognome,iscrizione_albo,specializzazione,citta):
            return render_template('Login.html')
        else: return render_template('RegistrazioneMedico.html')


@auth_blueprint.route('/registrazionePaziente', methods=['GET','POST'])
def registrazionePaziente():
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        nome=request.form.get('nome')
        cognome=request.form.get('cognome')
        CF=request.form.get('code')
        cellulare=request.form.get('cellulare')
        luogoNascita=request.form.get('cittanascita')
        domicilio=request.form.get('domicilio')
        dataNascita=request.form.get('datanascita')
        sesso=request.form.get('sesso')
        if AutenticazioneService.registrazionePaziente(email,password,nome,cognome,CF,cellulare,luogoNascita,domicilio,dataNascita,sesso):
            return render_template('HomePage.html')
        else: return render_template('RegistrazionePaziente.html')


@auth_blueprint.route('/registrazione/ente', methods=['GET','POST'])
def registrazioneEnte():
    if current_user.is_authenticated:
        return render_template('HomePage.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        password = request.form.get('password')
        citta = request.form.get('citta')
        if AutenticazioneService.registrazioneEnte(email,password,nome,citta):
            return render_template('HomePage.html')
        else: return render_template('RegistrazioneEnte.html')


@auth_blueprint.route('/logout')
def logout():
    return AutenticazioneService.logout()
