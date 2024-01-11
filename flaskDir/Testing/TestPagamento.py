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

# Paziente presente nel database
def test_mostraCarte1():
    with app.app_context():
        paziente = "MRSRSS029DGH6712"
        listaCarte = PagamentoService.getMetodi(paziente)
        assert all(metodopagamento.beneficiario == paziente for metodopagamento in listaCarte)

        oracolo = MetodoPagamento.query.filter_by(beneficiario=paziente).all()
        attributiOracolo = {(metodopagamento.CVV) for metodopagamento in oracolo}
        attributiListaCarte = {(metodopagamento.CVV) for metodopagamento in listaCarte}
        assert attributiOracolo == attributiListaCarte


# Paziente non presente nel database
def test_mostraCarte2():
    with app.app_context():
        paziente = "NTSASS02JDGH6563"
        listaCarte = PagamentoService.getMetodi(paziente)
        assert all(metodopagamento.beneficiario == paziente for metodopagamento in listaCarte)

        oracolo = MetodoPagamento.query.filter_by(beneficiario=paziente).all()
        attributiOracolo = {(metodopagamento.CVV) for metodopagamento in oracolo}
        attributiListaCarte = {(metodopagamento.CVV) for metodopagamento in listaCarte}
        assert attributiOracolo == attributiListaCarte


def test_eliminaCarta(client):
    with app.app_context():
        # Inserisci un metodo di pagamento di esempio nel database
        pan_di_test = '1234567890123456'
        metodo_di_test = MetodoPagamento(CVV=123, PAN=pan_di_test, nome_titolare='Nome Cognome', dataScadenza='01/2025', beneficiario='MRSRSS029DGH6712')
        db.session.add(metodo_di_test)
        db.session.commit()

        # Verifica che il metodo di pagamento sia stato inserito correttamente nel database
        assert MetodoPagamento.query.filter_by(PAN=pan_di_test).count() == 1

        # Chiamata al metodo eliminaMetodo
        PagamentoService.eliminaMetodo(pan_di_test)

        # Verifica che il metodo di pagamento sia stato eliminato correttamente
        assert MetodoPagamento.query.filter_by(PAN=pan_di_test).count() == 0



def test_addCarta(client):
    with app.app_context():
            cvv = 123
            pan = "8342645371625349"
            titolare = "Nome Cognome"
            mese = 12
            anno = 2024
            meseStr=str(mese)
            annoStr=str(anno)
            beneficiario = "MRSRSS029DGH6712"
            scadenza = meseStr+"/"+annoStr

            PagamentoService.addCarta(cvv,pan,titolare,scadenza,beneficiario)

            # Verifica che la carta sia stata inserita nel database
            carta_inserita = MetodoPagamento.query.filter_by(PAN='8342645371625349').first()
            assert carta_inserita is not None
            assert carta_inserita.nome_titolare == 'Nome Cognome'
            assert carta_inserita.dataScadenza == '12/2024'
            assert carta_inserita.beneficiario == 'MRSRSS029DGH6712'

            # Elimina la carta dal database una volta che il test e' stato eseguito
            MetodoPagamento.query.filter_by(PAN='8342645371625349').delete()
            db.session.commit()