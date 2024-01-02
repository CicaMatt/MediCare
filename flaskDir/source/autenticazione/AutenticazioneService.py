from flask import redirect, url_for, render_template, session
from flask_login import current_user, login_user, logout_user
import sqlalchemy
from flaskDir import db, app, login
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.prenotazioni.services import MedicoService

medicoService = MedicoService()
@login.user_loader
def load_user(id): #Bisogna aggiungere anche l'utente
    user_role = session['user_role']
    if user_role == 'paziente':
        return db.session.get(Paziente, id)

    elif user_role == 'medico':
        return db.session.get(Medico, id)
    elif user_role == 'ente':
        return db.session.get(EnteSanitario, id)


def login_page(request):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':  # Dovremmo controllare  giù la tipologia di accesso, es MEDICO
        email = request.form.get('email')
        password = request.form.get('password')
        medico = medicoService.retrieveMedico(email, password)
        if medico == None:
            return redirect(url_for('login'))  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(medico)  # Potremmo chidere anche se l'utente vuole essere ricordato
        session['user_role'] = 'medico'
        return redirect(url_for('home'))
    else:
        return render_template("Login.html")



def loginEnte_page(request):
    if current_user.is_authenticated:  # Aggiungere ROLE ENTE; ELSE ERROR
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email, EnteSanitario.password == password))
        if ente is None:
            return redirect(url_for('loginente'))  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(ente)  # Potremmo chidere anche se l'utente vuole essere ricordato
        session['user_role'] = 'ente'

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
        return redirect(url_for('login'))
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
        return redirect(url_for('loginente'))
    else:
        return render_template('RegistrazioneEnte.html')



def logout():
    logout_user()
    return redirect(url_for('home'))