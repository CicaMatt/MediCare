from flaskDir import db
from flask_login import UserMixin

class Paziente(db.Model, UserMixin):
    CF = db.Column(db.String(16), primary_key=True)
    chiaveSPID = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cognome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cellulare = db.Column(db.String(10), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    dataNascita = db.Column(db.Date, nullable=False)
    luogoNascita = db.Column(db.String(255), nullable=False)
    sesso = db.Column(db.String(30), nullable=False)
    carte = db.relationship("MetodoPagamento", backref="paziente",lazy=True)


