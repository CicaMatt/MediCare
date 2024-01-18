import pytest
from urllib.parse import quote

from flask import session
from flask_login import current_user

from flaskDir import app, db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.source.autenticazione import AutenticazioneService
from sqlalchemy_utils import create_database, database_exists


class TestAutenticazione:
    @pytest.fixture(autouse=True, scope='session')
    def setUp(self,request):
        # Configura il database di test
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('querty')}@localhost:3306/testmedicare"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["TESTING"] = True
        db.init_app(app)
        # Crea le tabelle del database di test
        with app.test_client():
            with app.app_context():
                #db.drop_all()

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



    def test_Validlogin_Medico(self):
        mail = "test@example1.com"
        password = "123password"
        new_user = Medico(
            email='test@example1.com',
            nome='John',
            cognome='Doe',
            iscrizione_albo=123242,
            specializzazione="chirurgia",
            città="Napoli",
            tariffa=50
        )
        new_user.set_password(password)
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()


        credenzialiTest = {"email": mail, "password": password, "tipo":"medico"}
        with app.test_client() as client:
            response = client.post('/auth/login', data=credenzialiTest)
            assert response.status_code == 302
            assert current_user.is_authenticated is True
            assert session.get('user_role') == "medico"



    def testfail_login_MedicoService(self):
        new_user = Medico(
            email='test@example.com',
            nome='John',
            cognome='Doe',
            iscrizione_albo=123242,
            specializzazione="chirurgia",
            città="Napoli",
            tariffa=50
        )
        new_user.set_password('123password')
        with app.app_context():

            user_in_db = AutenticazioneService.login_page(new_user.email, "123password", "medico")
            oracolo=False
            assert user_in_db==oracolo



    def test_emailInvalid_login(self):
        new_user = Medico(
            email='test@example.com',
            nome='John',
            cognome='Doe',
            iscrizione_albo=123242,
            specializzazione="chirurgia",
            città="Napoli",
            tariffa=50
        )
        new_user.set_password('123password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            user_in_db = AutenticazioneService.login_page("pincopalllo@gmail.com", "123password", "medico")
            oracolo = False
            assert user_in_db == oracolo
            db.session.delete(new_user)
            db.session.commit()

    def test_passwordInvalid_login(self):
        new_user = Medico(
            email='test@example.com',
            nome='John',
            cognome='Doe',
            iscrizione_albo=123242,
            specializzazione="chirurgia",
            città="Napoli",
            tariffa=50
        )
        new_user.set_password('123password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            user_in_db = AutenticazioneService.login_page("pincopalllo@gmail.com", "Pallino", "medico")
            oracolo = False
            assert user_in_db == oracolo
            db.session.delete(new_user)
            db.session.commit()




