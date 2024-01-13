import pytest
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.source.Pagamento.PagamentoService import PagamentoService


#pip install mysqlclient

@pytest.fixture(autouse=True)
def setUp():
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('Cancello1@')}@localhost:3306/testmedicare"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.app_context():
        # Drop all tables before creating the database
        db.drop_all()
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        # Create all tables after creating the database
        db.create_all()

def test_addCarta():
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

        # Verifica che la carta sia stata inserita nel database
        carta_inserita = MetodoPagamento.query.filter_by(PAN='8342645371625349', beneficiario="MRSRSS029DGH6712").first()
        assert carta_inserita is not None
        assert carta_inserita.nome_titolare == 'Nome Cognome'
        assert carta_inserita.dataScadenza == '12/2024'
        assert carta_inserita.beneficiario == 'MRSRSS029DGH6712'

        # Elimina la carta dal database una volta che il test e' stato eseguito
        MetodoPagamento.query.filter_by(PAN='8342645371625349', beneficiario="MRSRSS029DGH6712").delete()
        db.session.commit()



