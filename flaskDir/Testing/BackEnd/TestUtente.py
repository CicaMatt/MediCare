import datetime

import pytest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.Fascicolo.FascicoloService import FascicoloService
from flaskDir.source.Pagamento.PagamentoService import PagamentoService
from flaskDir.source.Utente.ISEEService import ISEEService


#pip install mysqlclient

@pytest.fixture(autouse=True, scope='session')
def setUp(request):
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('Cancello1@')}@localhost:3306/testmedicare"
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


def test_addDocumento():
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
    app.app_context().push()
    with app.app_context():
        num = 123
        tipo = 'Ricetta'
        data = datetime.date.today()
        descrizione = 'test'
        richiamo = None
        titolare = "PROVAS029DGH6712"

        FascicoloService.addDocumento(tipo,descrizione,richiamo,titolare)

        # Verifica che il documento sia stato inserito nel database di testmedicare
        quantiDocumenti = len(list(db.session.scalars(
            sqlalchemy.select(DocumentoSanitario).where(DocumentoSanitario.titolare == "PROVAS029DGH6712"))))
        assert quantiDocumenti==1
        oracoloNum = "FSE" + "0" + tipo[0]
        documento = DocumentoSanitario.query.filter_by(NumeroDocumento=oracoloNum).first()
        paziente=Paziente.query.filter_by(CF=titolare).first()
        assert documento is not None
        assert documento.titolare == 'PROVAS029DGH6712'
        assert documento.dataEmissione == datetime.date.today()
        assert documento.descrizione == 'test'
        assert  documento.tipo == 'Ricetta'

        db.session.delete(documento)
        db.session.delete(paziente)
        db.session.commit()



def test_getDocumentiSanitari():
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
        cf = mario.CF

        listaDocumenti = FascicoloService.getDocumentiSanitari(cf)
        assert all(documento.titolare == cf for documento in listaDocumenti)

        oracolo = DocumentoSanitario.query.filter_by(titolare=cf).all()
        attributiOracolo = {(documento.NumeroDocumento) for documento in oracolo}
        attributiListaDocumenti = {(documento.NumeroDocumento) for documento in listaDocumenti}
        assert attributiOracolo == attributiListaDocumenti

        db.session.delete(mario)
        db.session.commit()




def test_changeISEEFailure():
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

        result=ISEEService.changeISEE(mario.CF,new)

        paziente = Paziente.query.filter_by(CF=mario.CF).first()
        assert paziente.ISEE_ordinario is None
        assert result is False

        db.session.delete(paziente)
        db.session.commit()

def test_changeISEE():
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

        ISEEService.changeISEE(mario.CF,new)

        paziente = Paziente.query.filter_by(CF=mario.CF).first()
        assert paziente.ISEE_ordinario is not None
        assert paziente.ISEE_ordinario == new

        db.session.delete(paziente)
        db.session.commit()



