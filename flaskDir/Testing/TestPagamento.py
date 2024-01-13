import pytest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.source.Pagamento.PagamentoService import PagamentoService


#pip install mysqlclient

@pytest.fixture(autouse=True)
def setUp():
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI_TEST'] = f"mysql+pymysql://root:{quote('Cancello1@')}@localhost:3306/testmedicare"
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
        carta_inserita = MetodoPagamento.query.filter_by(PAN='8342645371625349', beneficiario="MRSRSS029DGH6712").first()
        assert carta_inserita is not None
        assert carta_inserita.nome_titolare == 'Nome Cognome'
        assert carta_inserita.dataScadenza == '12/2024'
        assert carta_inserita.beneficiario == 'MRSRSS029DGH6712'

        # Elimina la carta dal database una volta che il test è stato eseguito
        db.session.delete(carta_inserita)
        db.session.commit()



