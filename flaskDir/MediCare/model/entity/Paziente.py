from functools import wraps

import bcrypt
from flask import session, redirect, url_for

from flaskDir import db
from flask_login import UserMixin

def paziente_required(func):
    @wraps
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 'medico':
            return func(*args, **kwargs)
        return redirect(url_for('home'))
    return wrapper

class Paziente(db.Model, UserMixin):
    CF = db.Column(db.String(16), primary_key=True)
    chiaveSPID = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cognome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    cellulare = db.Column(db.String(10), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    dataNascita = db.Column(db.Date, nullable=False)
    luogoNascita = db.Column(db.String(255), nullable=False)
    sesso = db.Column(db.String(30), nullable=False)
    carte = db.relationship("MetodoPagamento", backref="paziente",lazy=True)


    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password_hash.encode('utf-8'))

    def get_id(self):
        return self.CF


