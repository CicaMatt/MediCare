from flaskDir import app, db

class EnteSanitario(db.Model):
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)

class Medico(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    cognome = db.Column(db.String(255))
    reparto = db.Column(db.String(255))
    ente_sanitario = db.Column(db.String(255), db.ForeignKey('ente_sanitario.email'), nullable=False)
    iscrizione_albo = db.Column(db.Integer)
    specializzazione = db.Column(db.String(255), nullable=False)

class Farmaco(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prezzo = db.Column(db.Float, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    __table_args__ = (db.UniqueConstraint('nome', 'categoria'),)

class Paziente(db.Model):
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

class MetodoPagamento(db.Model):
    CVV = db.Column(db.Integer, nullable=False)
    PAN = db.Column(db.String(16), nullable=False, primary_key=True)
    nome_titolare = db.Column(db.String(255), nullable=False)
    dataScadenza = db.Column(db.Date, nullable=False)
    beneficiario = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=False, primary_key=True)

class DocumentoSanitario(db.Model):
    NumeroDocumento = db.Column(db.String(20), nullable=False, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    dataEmissione = db.Column(db.Date, nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    titolare = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=True, primary_key=True)

class Prenotazione(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    oraVisita = db.Column(db.Integer, nullable=False)
    dataVisita = db.Column(db.Date, nullable=False)
    tipoVisita = db.Column(db.String(255), nullable=False)
    pazienteCF = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=True, primary_key=True)
    medico = db.Column(db.String(255), db.ForeignKey('medico.email'), nullable=True, primary_key=True)

class VisualizzaFarmaco(db.Model):
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Paziente = db.Column(db.String(16), db.ForeignKey('paziente.CF'), primary_key=True)

class ConsultaFarmaco(db.Model):
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)

class ConsultaFascicolo(db.Model):
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)
    Documento = db.Column(db.String(20), db.ForeignKey('documento_sanitario.NumeroDocumento'), primary_key=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
