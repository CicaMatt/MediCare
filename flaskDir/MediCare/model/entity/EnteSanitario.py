
from functools import wraps

from flask import session, redirect, url_for

from flaskDir import db, login
from flask_login import UserMixin

from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente


def ente_required(func):
    @wraps
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 'ente':
            return func(*args, **kwargs)
        return redirect(url_for('home'))
    return wrapper

class EnteSanitario(db.Model, UserMixin):
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    reparti = db.relationship("Medico", backref="reparti", lazy=True)

    def get_id(self):
        return self.email


    def get_id(self):
        return self.email