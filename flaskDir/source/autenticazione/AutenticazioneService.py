from flask import redirect, url_for, render_template
from flask_login import current_user, login_user, logout_user
import sqlalchemy
from flaskDir import db,app
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.source.prenotazioni.services import MedicoService

medicoService = MedicoService()

def login_page(request):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':  # Dovremmo controllare  giù la tipologia di accesso, es MEDICO
        email = request.form.get('email')
        password = request.form.get('password')
        medico = medicoService.retrieveMedico(email, password)
        if medico == None:
            return redirect(url_for('auth.login_page'))  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(medico)  # Potremmo chidere anche se l'utente vuole essere ricordato
        return redirect(url_for('home'))
    else:
        return render_template("Login.html")



def loginEnte_page(request):
    if current_user.is_authenticated:  # Aggiungere ROLE ENTE; ELSE ERROR
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email))
        if ente is None or not ente.check_password(password):
            redirect(url_for(
                'auth_blueprint.login_page'))  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(ente)  # Potremmo chidere anche se l'utente vuole essere ricordato
        return redirect(url_for('home'))
    else:
        return render_template("LoginEnte.html")



def registrazione_pageMedico(request):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email=request.form.get('email')

        password = request.form.get('password')
        nome=request.form.get('nome')
        cognome=request.form.get('cognome')
        iscrizione_albo=request.form.get('code')
        specializzazione=request.form.get('specializzazione')

        citta=request.form.get('citta')

        with app.app_context():
            medico=Medico()
            medico.email=email
            medico.set_password(password)
            medico.nome=nome
            medico.cognome=cognome
            medico.iscrizione_albo=int(iscrizione_albo)
            medico.specializzazione=specializzazione
            medico.città=citta
            db.session.add(medico)
            db.session.commit()
        return redirect(url_for('home'))
    else: return render_template('RegistrazioneMedico.html')





def registrazioneEnte(request):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        nome=request.form.get('nome')
        email=request.form.get('email')
        password=request.form.get('password')

        with app.app_context():
            ente=EnteSanitario()
            ente.nome=nome
            ente.email=email
            ente.password=password
            db.session.add(ente)
            db.session.commit()
        return redirect(url_for('auth.loginEnte_page'))



def logout():
    logout_user()
    return redirect(url_for('home'))