import pytest

from flaskDir import app
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.source.prenotazioni.services import PrenotazioneService


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
def test_paginaPrenotazioni(client):
    response = client.get("/prenotazione")
    assert response.status_code == 200

def test_paginaLogin(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_paginaRegistrazione(client):
    response = client.get('/registrazione')
    assert response.status_code == 200

def test_paginaVaccini(client):
    response = client.get('/vaccini')
    assert response.status_code == 200

def test_paginaFarmaci(client):
    response = client.get('/farmaci')
    assert response.status_code == 200

def test_dettagliFarmaco(client):
    response = client.get('/dettagliFarmaco')
    assert response.status_code == 200


#Controllare che solo l'ente possa accedervi!
def test_area_ente(client):
    response = client.get('/ente')
    assert response.status_code == 200

#Testare che solo l'ente possa accedervi!
def test_crea_medico(client):
    response = client.get('/creaMedico')
    assert response.status_code == 200


#Testare che solo l'utente possa accedervi!
def test_area_utente(client):
    response = client.get('/areaUtente')
    assert response.status_code == 200

def test_dati_sanitari(client):
    response = client.get('/datiSanitari')
    assert response.status_code == 200

def test_area_diagnostica(client):
    response = client.get('/areaDiagnostica')
    assert response.status_code == 200

def test_modifica_dati_utente(client):
    response = client.get('/modificaDatiUtente')
    assert response.status_code == 200

def test_lista_medici(client):
    response = client.get('/listamedici')
    assert response.status_code == 200


def test_prenotazioni_lista_medici_filtro(client):
    citta ="Napoli"
    specializzazione="chirurgia"
    parametri={"citta":citta,"specializzazione":specializzazione}
    response = client.get('/prenotazione/listamedici', query_string=parametri) #query string mette i parametri nella get

    listamedici = PrenotazioneService.getListaMedici("citta", citta)
    #Controllo che tutti i medici risultanti abbiano le caratteristiche scelte
    assert all(medico.città==citta and medico.specializzazione==specializzazione for medico in listamedici)
    #Controllo che i medici risultanti siano uguali all'oracolo
    assert set(listamedici) == set(Medico.query.filter_by(città=citta, specializzazione=specializzazione))



