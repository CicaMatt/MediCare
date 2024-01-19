from functools import wraps

import bcrypt
from flask import session, redirect, url_for

from flaskDir import db
from flaskDir import login
from flask_login import UserMixin

def medico_required(func):
    @wraps
    def wrapper(*args, **kwargs):
        """
        Decoratore per richiedere che l'utente abbia il ruolo di medico per accedere a determinate funzioni.

        Parametri:
        - func: Funzione da decorare.

        Returns:
        - Ritorna la funzione originale se l'utente ha il ruolo di medico, altrimenti reindirizza alla home.

        """
        if session.get('user_role') == 'medico':
            return func(*args, **kwargs)
        return redirect(url_for('home'))
    return wrapper

class Medico(db.Model, UserMixin):
    """
    Classe che rappresenta un medico nell'applicazione.

    Attributi:
    - email (str): Indirizzo email del medico (chiave primaria).
    - password_hash (str): Hash della password del medico.
    - nome (str): Nome del medico.
    - cognome (str): Cognome del medico.
    - reparto (str): Reparto in cui opera il medico.
    - ente_sanitario (str): Ente sanitario di appartenenza del medico (chiave esterna).
    - iscrizione_albo (int): Numero di iscrizione all'albo del medico.
    - specializzazione (str): Specializzazione del medico.
    - città (str): Città in cui opera il medico.
    - tariffa (Numeric): Tariffa del medico.
    - prenotazioni (relazione): Relazione con le prenotazioni associate al medico.

    Metodi:
    - set_password(password): Imposta la password del medico.
    - check_password(password): Verifica se la password fornita è corretta.
    - get_id(): Restituisce l'identificatore univoco del medico.

    """
    email = db.Column(db.String(255), primary_key=True)
    password_hash = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    cognome = db.Column(db.String(255))
    reparto = db.Column(db.String(255))
    ente_sanitario = db.Column(db.String(255), db.ForeignKey('ente_sanitario.email'), nullable=True)
    iscrizione_albo = db.Column(db.Integer)
    specializzazione = db.Column(db.String(255), nullable=False)
    città = db.Column(db.String(255), nullable=False)
    tariffa=db.Column(db.Numeric(precision=6, scale=2), nullable=False)
    prenotazioni=db.relationship('Prenotazione',backref="prenMed",lazy=True)

    def set_password(self, password):
        """
        Imposta la password del medico.

        Parametri:
        - password (str): Nuova password del medico.

        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed
    def check_password(self, password):
        """
        Verifica se la password fornita è corretta.

        Parametri:
        - password (str): Password da verificare.

        Ritorno:
        - bool: True se la password è corretta, False altrimenti.

        """
        return bcrypt.checkpw(password.encode('utf-8'),self.password_hash.encode('utf-8'))

    def get_id(self):
        """
        Restituisce l'identificativo unico del medico.

        Ritorno:
        - str: Identificativo unico del medico (indirizzo email).

        """
        return self.email