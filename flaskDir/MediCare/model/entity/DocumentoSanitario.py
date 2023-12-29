from flaskDir import db

class DocumentoSanitario(db.Model):
    NumeroDocumento = db.Column(db.String(20), nullable=False, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    dataEmissione = db.Column(db.Date, nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    titolare = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=True, primary_key=True)

