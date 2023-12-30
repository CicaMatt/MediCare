from flaskDir import db

class Medico(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    cognome = db.Column(db.String(255))
    reparto = db.Column(db.String(255))
    ente_sanitario = db.Column(db.String(255), db.ForeignKey('ente_sanitario.email'), nullable=True)
    iscrizione_albo = db.Column(db.Integer)
    specializzazione = db.Column(db.String(255), nullable=False)
    città = db.Column(db.String(255), nullable=False)
    prenotazioni=db.relationship('Prenotazione',backref="prenMed",lazy=True)
