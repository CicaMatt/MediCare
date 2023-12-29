from flaskDir import db

class ConsultaFascicolo(db.Model):
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)
    Documento = db.Column(db.String(20), db.ForeignKey('documento_sanitario.NumeroDocumento'), primary_key=True)

