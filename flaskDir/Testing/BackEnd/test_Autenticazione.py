from urllib.parse import quote

import pytest
from flask import session
from flask_login import current_user
from sqlalchemy_utils import create_database, database_exists

from flaskDir import app, db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.source.autenticazione import AutenticazioneService


class TestAutenticazione:
    @pytest.fixture(autouse=True, scope='session')
    def testapp(self,request):
        # Configura il database di test
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost:3306/testmedicare"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["TESTING"] = True
        db.init_app(app)
        # Crea le tabelle del database di test

    @pytest.fixture(autouse=True, scope='function')
    def setup_teardown(self):
        with app.test_client():
            with app.app_context():
                # db.drop_all()

                if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
                    create_database(app.config["SQLALCHEMY_DATABASE_URI"])

                db.create_all()
            yield
        # Tuo codice di tearDown qui
        with app.app_context():
            db.session.close_all()
            db.drop_all()

        # Aggiungi la funzione di tearDown alla richiesta


    def test_validlogin_medico(self):
        mail = "test@example1.com"
        password = "123password"
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password(password)
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        credenzialitest = {"email": mail, "password": password, "tipo": "medico"}
        with app.test_client() as client:
            response = client.post('/auth/login', data=credenzialitest)
            assert response.status_code == 302
            assert current_user.is_authenticated is True
            assert session.get('user_role') == "medico"

    def testfail_login_medicoservice(self):
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password('123password')
        with app.app_context():
            user_in_db = AutenticazioneService.login_page(new_user.email, "123password", "medico")
            oracolo = False
            assert user_in_db == oracolo

    def test_emailinvalidformat_login(self):
        mail = "test@exam"
        password = "123password"
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password(password)
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        credenzialitest = {"email": mail, "password": password, "tipo": "medico"}
        with app.test_client() as client:
            response = client.post('/auth/login', data=credenzialitest)
            assert not response.status_code == 302
            assert not current_user.is_authenticated is True
            assert not session.get('user_role') == "medico"

    def test_passwordinvalidformat_login(self):
        mail = "test@example.com"
        password = "123"
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password(password)
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        credenzialitest = {"email": mail, "password": password, "tipo": "medico"}
        with app.test_client() as client:
            response = client.post('/auth/login', data=credenzialitest)
            assert not response.status_code == 302
            assert not current_user.is_authenticated is True
            assert not session.get('user_role') == "medico"

    def test_emailinvalid_login(self):
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password('123password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            user_in_db = AutenticazioneService.login_page("pincopalllo@gmail.com", "123password", "medico")
            oracolo = False
            assert user_in_db == oracolo


    def test_passwordinvalid_login(self):
        new_user = Medico()
        new_user.email = 'test@example1.com'
        new_user.nome = 'John'
        new_user.cognome = 'Doe'
        new_user.iscrizione_albo = 123242
        new_user.specializzazione = "chrurgia"
        new_user.tariffa = 50
        new_user.città = "Napoli"
        new_user.set_password('123password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            user_in_db = AutenticazioneService.login_page("pincopalllo@gmail.com", "Pallino", "medico")
            oracolo = False
            assert user_in_db == oracolo
