import pytest
import sqlalchemy

from flaskDir import app, db
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento
from flaskDir.source.Pagamento.PagamentoService import PagamentoService


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client

#Paziente presente nel database
def test_mostraCarte1():
    with app.app_context():
        paziente = "MRSRSS029DGH6712"
        listaCarte = PagamentoService.getMetodi(paziente)
        assert all(metodopagamento.beneficiario == paziente for metodopagamento in listaCarte)

        oracolo = MetodoPagamento.query.filter_by(beneficiario=paziente).all()
        attributiOracolo = {(metodopagamento.CVV) for metodopagamento in oracolo}
        attributiListaCarte = {(metodopagamento.CVV) for metodopagamento in listaCarte}
        assert attributiOracolo == attributiListaCarte


#Paziente non presente nel database
def test_mostraCarte2():
    with app.app_context():
        paziente = "NTSASS029DGH6713"
        listaCarte = PagamentoService.getMetodi(paziente)
        assert all(metodopagamento.beneficiario == paziente for metodopagamento in listaCarte)

        oracolo = MetodoPagamento.query.filter_by(beneficiario=paziente).all()
        attributiOracolo = {(metodopagamento.CVV) for metodopagamento in oracolo}
        attributiListaCarte = {(metodopagamento.CVV) for metodopagamento in listaCarte}
        assert attributiOracolo == attributiListaCarte



def test_addCarta(client):
    with app.app_context():
        # Simula una richiesta POST con i dati necessari
        data = {
            'cvv': '123',
            'pan': '1234567890123456',
            'titolare': 'Nome Cognome',
            'mese': '01',
            'anno': '2025',
            'cf': 'MRSRSS029DGH6712'
        }

        # Stampa il percorso richiamato per debug
        print("Percorso richiamato:", '/addPagamento')

        response = client.post('/addPagamento', data=data, follow_redirects=True)

        # Verifica che la risposta sia stata ricevuta correttamente
        assert response.status_code == 200

        # Verifica che la carta sia stata inserita nel database
        carta_inserita = MetodoPagamento.query.filter_by(cvv='123', pan='1234567890123456').first()
        assert carta_inserita is not None
        assert carta_inserita.titolare == 'Nome Cognome'
        assert carta_inserita.scadenza == '01/2025'
        assert carta_inserita.beneficiario == 'MRSRSS029DGH6712'
