import pytest
import sqlalchemy
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from sqlalchemy_utils import create_database, database_exists

@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True, scope='session')
def setUp(request):
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('Gio210302DVK')}@localhost:3306/testmedicare"
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


def test_login_MedicoService():
    new_user = Medico(
        email='test@example.com',
        password_hash='password123',
        nome='John',
        cognome='Doe',
        iscrizione_albo=123242,
        specializzazione="chirurgia",
        città="Napoli",
        tariffa=50
    )
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

        user_in_db = Medico.query.filter_by(email='test@example.com').first()
        assert user_in_db
        db.session.delete(user_in_db)
        db.session.commit()



def testfail_login_MedicoService():
    new_user = Medico(
        email='test@example.com',
        password_hash='password123',
        nome='John',
        cognome='Doe',
        iscrizione_albo=123242,
        specializzazione="chirurgia",
        città="Napoli",
        tariffa=50
    )
    with app.app_context():

        user_in_db = Medico.query.filter_by(email='test@example.com').first()
        oracolo=None
        assert user_in_db==oracolo


