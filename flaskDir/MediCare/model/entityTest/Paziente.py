from functools import wraps

import bcrypt
from flask import session, redirect, url_for

from flaskDir import test
from flask_login import UserMixin

def paziente_required(func):
    @wraps
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 'medico':
            return func(*args, **kwargs)
        return redirect(url_for('home'))
    return wrapper

class Paziente(test.Model, UserMixin):
    CF = test.Column(test.String(16), primary_key=True)
    chiaveSPID = test.Column(test.Integer, nullable=False)
    nome = test.Column(test.String(255), nullable=False)
    cognome = test.Column(test.String(255), nullable=False)
    email = test.Column(test.String(255), nullable=False)
    password_hash = test.Column(test.String(255), nullable=False)
    cellulare = test.Column(test.String(10), nullable=False)
    domicilio = test.Column(test.String(255), nullable=False)
    dataNascita = test.Column(test.Date, nullable=False)
    luogoNascita = test.Column(test.String(255), nullable=False)
    sesso = test.Column(test.String(30), nullable=False)
    ISEE_ordinario = test.Column(test.Numeric(precision=9,scale=2), nullable =True)#cambiare salvataggio di un paziente nei services
    carte = test.relationship("MetodoPagamento", backref="paziente",lazy=True)


    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password_hash.encode('utf-8'))

    def get_id(self):
        return self.CF


