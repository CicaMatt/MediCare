from flaskDir import db

class Prenotazione(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    oraVisita = db.Column(db.Integer, nullable=False)
    dataVisita = db.Column(db.Date, nullable=False)
    tipoVisita = db.Column(db.String(255), nullable=False)
    pazienteCF = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=True, primary_key=True)
    medico = db.Column(db.String(255), db.ForeignKey('medico.email'), nullable=True, primary_key=True)
