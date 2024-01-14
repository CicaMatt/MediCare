import pytest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.source.Pagamento.PagamentoService import PagamentoService


#pip install mysqlclient

@pytest.fixture(autouse=True)
def setUp():
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI_TEST'] = f"mysql+pymysql://root:{quote('Gio210302DVK')}@localhost:3306/testmedicare"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS_TEST"] = False
    # Crea le tabelle del database di test
    with app.app_context():
        db.drop_all()
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI_TEST"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI_TEST"])

        db.create_all()

def test_addCarta():
    # Cambia il URI del database a quello di test
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI_TEST']

    with app.app_context():
        mario=Paziente()
        mario.nome="Mario"
        mario.cognome="Rossi"
        mario.email="mariorossi@gmail.com"
        mario.password_hash="rosso10"
        mario.chiaveSPID=10
        mario.ISEE_ordinario=10000
        mario.CF="MRSRSS029DGH6712"
        mario.cellulare="3312258345"
        mario.luogoNascita="Salerno"
        mario.dataNascita="2000-12-31"
        mario.domicilio="Salerno"
        mario.sesso="Maschio"
        db.session.add(mario)
        db.session.commit()
    app.app_context().push()
    with app.app_context():
        cvv = 123
        pan = "8342645371625349"
        titolare = "Nome Cognome"
        mese = 12
        anno = 2024
        meseStr = str(mese)
        annoStr = str(anno)
        beneficiario = "MRSRSS029DGH6712"
        scadenza = meseStr + "/" + annoStr

        PagamentoService.addCarta(cvv, pan, titolare, scadenza, beneficiario)

        # Verifica che la carta sia stata inserita nel database di testmedicare
        carta_inserita = MetodoPagamento.query.filter_by(PAN=pan, beneficiario=beneficiario).first()
        paziente=Paziente.query.filter_by(CF=beneficiario).first()
        assert carta_inserita is not None
        assert carta_inserita.nome_titolare == 'Nome Cognome'
        assert carta_inserita.dataScadenza == '12/2024'
        assert carta_inserita.beneficiario == 'MRSRSS029DGH6712'

        # Elimina la carta dal database una volta che il test è stato eseguito
        db.session.delete(paziente)
        db.session.delete(carta_inserita)
        db.session.commit()



