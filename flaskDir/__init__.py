
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Gio210302DVK@localhost:3306/medicare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
# Modello EnteSanitario
class EnteSanitario(db.Model):
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)

# Modello Medico
class Medico(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    cognome = db.Column(db.String(255))
    reparto = db.Column(db.String(255))
    ente_sanitario = db.Column(db.String(255), db.ForeignKey('ente_sanitario.email'), nullable=False)
    iscrizione_albo = db.Column(db.Integer)
    specializzazione = db.Column(db.String(255), nullable=False)

# Modello Farmaco
class Farmaco(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prezzo = db.Column(db.Float, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    descrizione = db.Column(db.Text, nullable=False)

# Modello Paziente
class Paziente(db.Model):
    cf = db.Column(db.String(16), primary_key=True)
    chiave_spid = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cognome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cellulare = db.Column(db.String(10), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    data_nascita = db.Column(db.Date, nullable=False)
    luogo_nascita = db.Column(db.String(255), nullable=False)
    sesso = db.Column(db.String(30), nullable=False)

# Modello MetodoPagamento
class MetodoPagamento(db.Model):
    cvv = db.Column(db.Integer, nullable=False)
    pan = db.Column(db.String(16), nullable=False, primary_key=True)
    nome_titolare = db.Column(db.String(255), nullable=False)
    data_scadenza = db.Column(db.Date, nullable=False)
    beneficiario = db.Column(db.String(16), db.ForeignKey('paziente.cf'), nullable=False, primary_key=True)

# Modello DocumentoSanitario
class DocumentoSanitario(db.Model):
    numero_documento = db.Column(db.String(20), nullable=False, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    data_emissione = db.Column(db.Date, nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    titolare = db.Column(db.String(16), db.ForeignKey('paziente.cf'), nullable=True, primary_key=True)

# Modello Prenotazione
class Prenotazione(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ora_visita = db.Column(db.Integer, nullable=False)
    data_visita = db.Column(db.Date, nullable=False)
    tipo_visita = db.Column(db.String(255), nullable=False)
    paziente_cf = db.Column(db.String(16), db.ForeignKey('paziente.cf'), nullable=True, primary_key=True)
    medico = db.Column(db.String(255), db.ForeignKey('medico.email'), nullable=True, primary_key=True)

# Modello VisualizzaFarmaco
class VisualizzaFarmaco(db.Model):
    farmaco_id = db.Column(db.Integer, db.ForeignKey('farmaco.id'), primary_key=True)
    paziente_cf = db.Column(db.String(16), db.ForeignKey('paziente.cf'), primary_key=True)

# Modello ConsultaFarmaco
class ConsultaFarmaco(db.Model):
    farmaco_id = db.Column(db.Integer, db.ForeignKey('farmaco.id'), primary_key=True)
    medico_email = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)

# Modello ConsultaFascicolo
class ConsultaFascicolo(db.Model):
    medico_email = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)
    documento_numero = db.Column(db.String(20), db.ForeignKey('documento_sanitario.numero_documento'), primary_key=True)


with app.app_context():
    db.create_all()


