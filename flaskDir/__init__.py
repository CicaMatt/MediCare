from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from urllib.parse import quote

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('Cancello1@')}@localhost:3306/medicare"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
login = LoginManager(app)


from flaskDir.MediCare.model.entity import Paziente, Farmaco, Medici, Prenotazione, MetodoPagamento, DocumentoSanitario, \
    EnteSanitario, ConsultaFarmaco, VisualizzaFarmaco, AutorizzazioniFSE

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()
else:
    with app.app_context():
        db.create_all()




app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('Cancello1@')}@localhost:3306/testmedicare"

test = SQLAlchemy(app)
test.init_app(app)


from flaskDir.MediCare.model.entityTest import Paziente, Farmaco, Medici, Prenotazione, MetodoPagamento, DocumentoSanitario, \
    EnteSanitario, ConsultaFarmaco, VisualizzaFarmaco, AutorizzazioniFSE

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        test.create_all()
else:
    with app.app_context():
        test.create_all()

from flaskDir import routes