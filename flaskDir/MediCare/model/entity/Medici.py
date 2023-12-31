import bcrypt

from flaskDir import db
from flaskDir import login
from flask_login import UserMixin


@login.user_loader
def load_user(id): #Bisogna aggiungere anche l'utente
    return db.session.get(Medico, id)



class Medico(db.Model, UserMixin):
    email = db.Column(db.String(255), primary_key=True)
    password_hash = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    cognome = db.Column(db.String(255))
    reparto = db.Column(db.String(255))
    ente_sanitario = db.Column(db.String(255), db.ForeignKey('ente_sanitario.email'), nullable=True)
    iscrizione_albo = db.Column(db.Integer)
    specializzazione = db.Column(db.String(255), nullable=False)
    città = db.Column(db.String(255), nullable=False)
    prenotazioni=db.relationship('Prenotazione',backref="prenMed",lazy=True)

    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password_hash.encode('utf-8'))

    def get_id(self):
        return self.email