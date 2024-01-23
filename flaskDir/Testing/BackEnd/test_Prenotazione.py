import pytest
from flaskDir import app, db
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from sqlalchemy_utils import create_database, database_exists

from flaskDir.source.prenotazioni.PrenotazioneService import PrenotazioneService


class TestPrenotazione:
    @pytest.fixture(autouse=True, scope='session')
    def setup(self, request):
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

    def test_dateinvalidprenotazione(self):
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

                medico = Medico()
                medico.email = "test@example1.com"
                medico.nome = "John"
                medico.cognome = "Doe"
                medico.iscrizione_albo = 123242
                medico.specializzazione = "chirurigia"
                medico.tariffa = 50
                medico.città = "Napoli"
                medico.set_password("123password")
                db.session.add(mario)
                db.session.add(medico)
                db.session.commit()

                oravisita = "11"
                datavisita = "44"
                tipovisita = "chirurgia"
                prezzo = 50
                pazientecf = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, datavisita, oravisita, tipovisita, pazientecf,
                                                              prezzo, "Select")
                oracle = False
                assert oracle == result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_orainvalidprenotazione(self):
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

                medico = Medico()
                medico.email = "test@example1.com"
                medico.nome = "John"
                medico.cognome = "Doe"
                medico.iscrizione_albo = 123242
                medico.specializzazione = "chirurigia"
                medico.tariffa = 50
                medico.città = "Napoli"
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "100"
                datavisita = "10"
                tipovisita = "Oculistica"
                prezzo = 50
                pazientecf = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, datavisita, oravisita, tipovisita, pazientecf,
                                                              prezzo, "Select")
                oracle = False
                assert oracle == result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_prezzoneg(self):
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

                medico = Medico()
                medico.email = "test@example1.com"
                medico.nome = "John"
                medico.cognome = "Doe"
                medico.iscrizione_albo = 123242
                medico.specializzazione = "chirurigia"
                medico.tariffa = 50
                medico.città = "Napoli"
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                datavisita = "10"
                tipovisita = "Oculistica"
                prezzo = -200
                pazientecf = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, datavisita, oravisita, tipovisita, pazientecf,
                                                              prezzo, "Select")
                oracle = False
                assert oracle == result
                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_cartainvalid(self):
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

                medico = Medico()
                medico.email = "test@example1.com"
                medico.nome = "John"
                medico.cognome = "Doe"
                medico.iscrizione_albo = 123242
                medico.specializzazione = "chirurigia"
                medico.tariffa = 50
                medico.città = "Napoli"
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                datavisita = "10"
                tipovisita = "Oculistica"
                prezzo = 200
                pazientecf = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, datavisita, oravisita, tipovisita, pazientecf,
                                                              prezzo, "AB523")
                oracle = None
                assert oracle == result
                prenotazione = Prenotazione.query.filter_by(pazienteCF=pazientecf, medico=idmedico).first()
                assert prenotazione
                assert not prenotazione.pagata
                db.session.delete(prenotazione)
                db.session.commit()

                db.session.delete(mario)
                db.session.delete(medico)
                db.session.commit()

    def test_prenotazionesaved(self):
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

                medico = Medico()
                medico.email = "test@example1.com"
                medico.nome = "John"
                medico.cognome = "Doe"
                medico.iscrizione_albo = 123242
                medico.specializzazione = "chirurigia"
                medico.tariffa = 50
                medico.città = "Napoli"
                medico.set_password("123password")
                db.session.add(medico)
                db.session.add(mario)
                db.session.commit()

                oravisita = "10"
                datavisita = "10"
                tipovisita = "Oculistica"
                prezzo = 50
                pazientecf = mario.CF
                idmedico = medico.email

                result = PrenotazioneService.savePrenotazione(idmedico, datavisita, oravisita, tipovisita, pazientecf,
                                                              prezzo, "Select")
                oracle = None
                assert oracle == result
                prenotazione = Prenotazione.query.filter_by(pazienteCF=pazientecf, medico=idmedico).first()
                assert prenotazione is not None

                db.session.delete(prenotazione)
                db.session.commit()
                db.session.delete(medico)
                db.session.delete(mario)
                db.session.commit()
