from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_utils import create_database, database_exists

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lollipop@localhost:3306/medicare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

from flaskDir.MediCare.model.entity import Paziente, Farmaco, Medici, Prenotazione, MetodoPagamento, DocumentoSanitario, \
    EnteSanitario, ConsultaFarmaco, VisualizzaFarmaco, AutorizzazioniFSE

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()
else:
    with app.app_context():
        db.create_all()

from flaskDir import routes
