from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user, login_user, logout_user
import sqlalchemy
from flaskDir import db,app
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.source.prenotazioni.services import MedicoService

auth_blueprint = Blueprint('authBluePrint', __name__)

medicoService = MedicoService()


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':  # Dovremmo controllare  giù la tipologia di accesso, es MEDICO
        email = request.form.get('email')
        password = request.form.get('password')
        medico = medicoService.retrieveMedico(email, password)
        if medico == None:
            return redirect(url_for('authBluePrint.login_page'))  # Gli potrei aggiungere la notifica che le credenziali son oerrate
        login_user(medico)  # Potremmo chidere anche se l'utente vuole essere ricordato
        return redirect(url_for('home'))
    else:
        return render_template("Login.html")


@auth_blueprint.route('/loginENTE', methods=['GET', 'POST'])
def loginEnte_page():
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


@auth_blueprint.route('/registrazione', methods=['GET', 'POST'])
def registrazione_page():
    if current_user.is_authenticated:
        return redirect(url_for('home'))


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
