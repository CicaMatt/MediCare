from flaskDir import db

class MetodoPagamento(db.Model):
    CVV = db.Column(db.Integer, nullable=False)
    PAN = db.Column(db.String(16), nullable=False, primary_key=True)
    nome_titolare = db.Column(db.String(255), nullable=False)
    cognome_titolare = db.Column(db.String(255), nullable=False)
    dataScadenza = db.Column(db.Date, nullable=False)
    beneficiario = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=False, primary_key=True)

