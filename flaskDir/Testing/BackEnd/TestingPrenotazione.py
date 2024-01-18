import pytest
from flask import session
from flask_login import current_user
from flaskDir import app, db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.source.prenotazioni.services import PrenotazioneService
from sqlalchemy_utils import create_database, database_exists


class TestPrenotazione():
    @pytest.fixture(autouse=True, scope='session')
    def setUp(self, request):
        # Configura il database di test
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root@localhost:3306/testmedicare"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["TESTING"] = True
        db.init_app(app)
        # Crea le tabelle del database di test
        with app.test_client():
            with app.app_context():
                # db.drop_all()

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


    def test_DateInvalidprenotazione(self):
        with app.test_client():
            with app.app_context():
                mario = Paziente()
                mario.nome = "Mario"
                mario.cognome = "Rossi"
                mario.email = "mariorossi@gmail.com"
                mario.password_hash = "cancello"
                mario.chiaveSPID = 10
                mario.ISEE_ordinario = 10000
                mario.CF = "PROVAS029DGH6712"
                mario.cellulare = "3312258345"
                mario.luogoNascita = "Salerno"
                mario.dataNascita = "2000-12-31"
                mario.domicilio = "Salerno"
                mario.sesso = "Maschio"

                medico = Medico(
                    email='test@example1.com',
                    nome='John',
                    cognome='Doe',
                    iscrizione_albo=123242,
                    specializzazione="chirurgia",
                    città="Napoli",
                    tariffa=50
                )
                medico.set_password("123password")
                db.session.add(mario)
                db.session.add(medico)
                db.session.commit()


                oravisita="11"
                dataVisita="44"
                tipoVisita="chirurgia"
                prezzo=50
                pazienteCF=mario.CF
                idmedico=medico.email

                result=PrenotazioneService.savePrenotazione(idmedico,dataVisita,oravisita,tipoVisita,pazienteCF,prezzo,"Select")
                oracle=False
                assert oracle==result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()


    def test_OraInvalidprenotazione(self):
        with app.test_client():
            with app.app_context():
                mario = Paziente()
                mario.nome = "Mario"
                mario.cognome = "Rossi"
                mario.email = "mariorossi@gmail.com"
                mario.password_hash = "cancello"
                mario.chiaveSPID = 10
                mario.ISEE_ordinario = 10000
                mario.CF = "PROVAS029DGH6712"
                mario.cellulare = "3312258345"
                mario.luogoNascita = "Salerno"
                mario.dataNascita = "2000-12-31"
                mario.domicilio = "Salerno"
                mario.sesso = "Maschio"

                medico = Medico(
                    email='test@example1.com',
                    nome='John',
                    cognome='Doe',
                    iscrizione_albo=123242,
                    specializzazione="chirurgia",
                    città="Napoli",
                    tariffa=50
                )
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "100"
                dataVisita = "10"
                tipoVisita = "Oculistica"
                prezzo = 50
                pazienteCF = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, dataVisita, oravisita, tipoVisita, pazienteCF,
                                                              prezzo, "Select")
                oracle = False
                assert oracle == result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()


    def test_prezzoNeg(self):
        with app.test_client():
            with app.app_context():
                mario = Paziente()
                mario.nome = "Mario"
                mario.cognome = "Rossi"
                mario.email = "mariorossi@gmail.com"
                mario.password_hash = "cancello"
                mario.chiaveSPID = 10
                mario.ISEE_ordinario = 10000
                mario.CF = "PROVAS029DGH6712"
                mario.cellulare = "3312258345"
                mario.luogoNascita = "Salerno"
                mario.dataNascita = "2000-12-31"
                mario.domicilio = "Salerno"
                mario.sesso = "Maschio"

                medico = Medico(
                    email='test@example1.com',
                    nome='John',
                    cognome='Doe',
                    iscrizione_albo=123242,
                    specializzazione="chirurgia",
                    città="Napoli",
                    tariffa=50
                )
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                dataVisita = "10"
                tipoVisita = "Oculistica"
                prezzo = -200
                pazienteCF = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, dataVisita, oravisita, tipoVisita, pazienteCF,
                                                              prezzo, "Select")
                oracle = False
                assert oracle == result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_cartaInvalid(self):
        with app.test_client():
            with app.app_context():
                mario = Paziente()
                mario.nome = "Mario"
                mario.cognome = "Rossi"
                mario.email = "mariorossi@gmail.com"
                mario.password_hash = "cancello"
                mario.chiaveSPID = 10
                mario.ISEE_ordinario = 10000
                mario.CF = "PROVAS029DGH6712"
                mario.cellulare = "3312258345"
                mario.luogoNascita = "Salerno"
                mario.dataNascita = "2000-12-31"
                mario.domicilio = "Salerno"
                mario.sesso = "Maschio"

                medico = Medico(
                    email='test@example1.com',
                    nome='John',
                    cognome='Doe',
                    iscrizione_albo=123242,
                    specializzazione="chirurgia",
                    città="Napoli",
                    tariffa=50
                )
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                dataVisita = "10"
                tipoVisita = "Oculistica"
                prezzo = 200
                pazienteCF = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, dataVisita, oravisita, tipoVisita, pazienteCF,
                                                              prezzo, "AB523")
                oracle = None
                assert oracle == result
                prenotazione = Prenotazione.query.filter_by(pazienteCF=pazienteCF, medico=idmedico).first()
                assert prenotazione
                assert not prenotazione.pagata
                db.session.delete(prenotazione)
                db.session.commit()

                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_PrenotazioneSaved(self):
        with app.test_client():
            with app.app_context():
                mario = Paziente()
                mario.nome = "Mario"
                mario.cognome = "Rossi"
                mario.email = "mariorossi@gmail.com"
                mario.password_hash = "cancello"
                mario.chiaveSPID = 10
                mario.ISEE_ordinario = 10000
                mario.CF = "PROVAS029DGH6712"
                mario.cellulare = "3312258345"
                mario.luogoNascita = "Salerno"
                mario.dataNascita = "2000-12-31"
                mario.domicilio = "Salerno"
                mario.sesso = "Maschio"

                medico = Medico(
                    email='test@example1.com',
                    nome='John',
                    cognome='Doe',
                    iscrizione_albo=123242,
                    specializzazione="chirurgia",
                    città="Napoli",
                    tariffa=50
                )
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                dataVisita = "10"
                tipoVisita = "Oculistica"
                prezzo = 50
                pazienteCF = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, dataVisita, oravisita, tipoVisita, pazienteCF,
                                                              prezzo, "Select")
                oracle = None
                assert oracle == result
                prenotazione = Prenotazione.query.filter_by(pazienteCF=pazienteCF, medico=idmedico).first()
                assert prenotazione is not None

                db.session.delete(prenotazione)
                db.session.commit()
                db.session.delete(medico)
                db.session.delete(mario)
                db.session.commit()





