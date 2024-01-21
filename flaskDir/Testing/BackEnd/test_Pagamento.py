import pytest
from sqlalchemy_utils import database_exists, create_database
from flaskDir import app, db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.Pagamento.PagamentoService import PagamentoService


@pytest.fixture(autouse=True, scope='session')
def setup(request):
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root@localhost:3306/testmedicare"
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


# Formato PAN non valido
def test_addcarta1():
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
        db.session.add(mario)
        db.session.commit()

    with app.app_context():
        cvv = 123
        pan = "83426453716253494"
        titolare = "Nome Cognome"
        mese = 12
        anno = 2024
        mesestr = str(mese)
        annostr = str(anno)
        beneficiario = "PROVAS029DGH6712"
        scadenza = mesestr + "/" + annostr

        PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)

        # Verifica che la carta non sia stata inserita nel database di testmedicare
        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente = Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is None

        db.session.delete(paziente)
        db.session.commit()


# Formato Data non valido
def test_addcarta2():
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
        db.session.add(mario)
        db.session.commit()

    with app.app_context():
        cvv = 123
        pan = "8342645371625349"
        titolare = "Nome Cognome"
        mese = 13
        anno = 2024
        mesestr = str(mese)
        annostr = str(anno)
        beneficiario = "PROVAS029DGH6712"
        scadenza = mesestr + "/" + annostr

        PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)

        # Verifica che la carta non sia stata inserita nel database di testmedicare
        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente = Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is None

        db.session.delete(paziente)
        db.session.commit()


# Formato CVV non valido
def test_addcarta3():
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
        db.session.add(mario)
        db.session.commit()

    with app.app_context():
        cvv = 1234
        pan = "8342645371625349"
        titolare = "Nome Cognome"
        mese = 12
        anno = 2024
        mesestr = str(mese)
        annostr = str(anno)
        beneficiario = "PROVAS029DGH6712"
        scadenza = mesestr + "/" + annostr

        PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)

        # Verifica che la carta non sia stata inserita nel database di testmedicare
        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente = Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is None

        db.session.delete(paziente)
        db.session.commit()


# Carta gia presente nel db
def test_addcarta4():
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
        db.session.add(mario)
        db.session.commit()

    with app.app_context():
        carta = MetodoPagamento()
        carta.CVV = 123
        carta.PAN = "8342645371625349"
        carta.nome_titolare = "Nome Cognome"
        carta.dataScadenza = 12/2024
        carta.beneficiario = "PROVAS029DGH6712"
        db.session.add(carta)
        db.session.commit()

    with app.app_context():
        cvv = 123
        pan = "8342645371625349"
        titolare = "Nome Cognome"
        mese = 12
        anno = 2024
        mesestr = str(mese)
        annostr = str(anno)
        beneficiario = "PROVAS029DGH6712"
        scadenza = mesestr + "/" + annostr

        cartanew = PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)
        assert cartanew is None

        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente = Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is not None

        db.session.delete(carta_inserita)
        db.session.delete(paziente)
        db.session.commit()


# Caso di successo
def test_addcartasuccess():
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
        db.session.add(mario)
        db.session.commit()

    with app.app_context():
        cvv = 123
        pan = "8342645371625349"
        titolare = "Nome Cognome"
        mese = 12
        anno = 2024
        mesestr = str(mese)
        annostr = str(anno)
        beneficiario = "PROVAS029DGH6712"
        scadenza = mesestr + "/" + annostr

        PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)

        # Verifica che la carta sia stata inserita nel database di testmedicare
        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente = Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is not None
        assert carta_inserita.nome_titolare == 'Nome Cognome'
        assert carta_inserita.dataScadenza == '12/2024'
        assert carta_inserita.beneficiario == 'PROVAS029DGH6712'

        db.session.delete(carta_inserita)
        db.session.delete(paziente)
        db.session.commit()



'''

TEST IN PIU'
 
# Paziente presente nel database
def test_mostracarte1():
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
        db.session.add(mario)
        db.session.commit()
        cf = mario.CF

        metodo_di_test = MetodoPagamento(CVV=123, PAN='1234567890123456', nome_titolare='Nome Cognome',
                                         dataScadenza='01/2025', beneficiario='PROVAS029DGH6712')
        db.session.add(metodo_di_test)
        db.session.commit()

        listacarte = list(PagamentoService.getMetodi(cf))

        assert all(metodopagamento.beneficiario == cf for metodopagamento in listacarte)
        oracolo = MetodoPagamento.query.filter_by(beneficiario=cf).all()
        attributioracolo = {metodopagamento.PAN for metodopagamento in oracolo}
        attributilistacarte = {metodopagamento.PAN for metodopagamento in listacarte}
        assert attributioracolo == attributilistacarte

        db.session.delete(metodo_di_test)
        db.session.delete(mario)
        db.session.commit()


# Paziente non presente nel database
def test_mostracarte2():
    with app.app_context():
        paziente = "NTSASS02JDGH6563"
        listacarte = PagamentoService.getMetodi(paziente)
        assert all(metodopagamento.beneficiario == paziente for metodopagamento in listacarte)

        oracolo = MetodoPagamento.query.filter_by(beneficiario=paziente).all()
        attributioracolo = {metodopagamento.CVV for metodopagamento in oracolo}
        attributilistacarte = {metodopagamento.CVV for metodopagamento in listacarte}
        assert attributioracolo == attributilistacarte



def test_eliminacarta():

    with app.app_context():
        # Inserisci un metodo di pagamento di esempio nel database
        pan_di_test = '1234567890123456'
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
        db.session.add(mario)
        db.session.commit()

        paziente_test = Paziente.query.filter_by(CF="PROVAS029DGH6712").first()
        metodo_di_test = MetodoPagamento(CVV=123, PAN=pan_di_test, nome_titolare='Nome Cognome', dataScadenza='01/2025',
                                         beneficiario='PROVAS029DGH6712')
        db.session.add(metodo_di_test)
        db.session.commit()

        # Verifica che il metodo di pagamento sia stato inserito correttamente nel database
        assert MetodoPagamento.query.filter_by(PAN=pan_di_test, beneficiario=paziente_test.CF).count() == 1

        # Chiamata al metodo eliminaMetodo
        PagamentoService.eliminaMetodo(pan_di_test, paziente_test.CF)

        # Verifica che il metodo di pagamento sia stato eliminato correttamente
        assert MetodoPagamento.query.filter_by(PAN=pan_di_test).count() == 0

        db.session.delete(metodo_di_test)
        db.session.delete(mario)
        db.session.commit()


'''