import datetime

import pytest
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from flaskDir import app, db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.Utente.FascicoloService import FascicoloService
from flaskDir.source.Utente.ISEEService import ISEEService


class TestUtente:
    @pytest.fixture(autouse=True, scope='session')
    def setup(self,request):
        # Configura il database di test
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost:3306/testmedicare"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["TESTING"] = True
        db.init_app(app)
        # Crea le tabelle del database di test
        with app.test_client():
            with app.app_context():

                if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
                    create_database(app.config["SQLALCHEMY_DATABASE_URI"])

                db.create_all()

        def teardown():
            # Tuo codice di tearDown qui
            with app.app_context():
                db.session.close_all()
                db.drop_all()

        # Aggiungi la funzione di tearDown alla richiesta
        request.addfinalizer(teardown)

    def test_changeiseefailure(self):
        with app.app_context():
            mario = Paziente()
            mario.nome = "Mario"
            mario.cognome = "Rossi"
            mario.email = "mariorossi@gmail.com"
            mario.password_hash = "cancello"
            mario.chiaveSPID = 10
            mario.ISEE_ordinario = None
            mario.CF = "PROVAS029DGH6712"
            mario.cellulare = "3312258345"
            mario.luogoNascita = "Salerno"
            mario.dataNascita = "2000-12-31"
            mario.domicilio = "Salerno"
            mario.sesso = "Maschio"
            db.session.add(mario)
            db.session.commit()

            new = -10000

            result = ISEEService.changeISEE(mario.CF, new)

            paziente = Paziente.query.filter_by(CF=mario.CF).first()
            assert paziente.ISEE_ordinario is None
            assert result is False

            db.session.delete(paziente)
            db.session.commit()

    def test_changeisee(self):
        with app.app_context():
            mario = Paziente()
            mario.nome = "Mario"
            mario.cognome = "Rossi"
            mario.email = "mariorossi@gmail.com"
            mario.password_hash = "cancello"
            mario.chiaveSPID = 10
            mario.ISEE_ordinario = None
            mario.CF = "PROVAS029DGH6712"
            mario.cellulare = "3312258345"
            mario.luogoNascita = "Salerno"
            mario.dataNascita = "2000-12-31"
            mario.domicilio = "Salerno"
            mario.sesso = "Maschio"
            db.session.add(mario)
            db.session.commit()

            new = 10000

            ISEEService.changeISEE(mario.CF, new)

            paziente = Paziente.query.filter_by(CF=mario.CF).first()
            assert paziente.ISEE_ordinario is not None
            assert paziente.ISEE_ordinario == new

            db.session.delete(paziente)
            db.session.commit()



