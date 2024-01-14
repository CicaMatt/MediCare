import pytest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from flaskDir import app, db
from flaskDir.MediCare.model.entity.Farmaco import Farmaco
from flaskDir.source.Farmaci.FarmaciService import FarmaciService





#pip install mysqlclient


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client




#test con inserimento di categoria e prezzo
def test_filtroCatalogoFarmaci(client):

    with app.app_context():
        categoria = "Sciroppo"
        prezzo = 0

        listafarmaci = FarmaciService.filtraCatalogo(categoria, prezzo)

        # Controllo che tutti i farmaci risultanti abbiano le caratteristiche scelte
        assert all(farmaco.categoria == categoria and farmaco.prezzo == prezzo for farmaco in listafarmaci)

        # Controllo che i farmaci risultanti siano uguali all'oracolo
        oracolo = Farmaco.query.filter_by(categoria=categoria, prezzo=prezzo).all()
        attributi_oracolo = {(farmaco.nome) for farmaco in oracolo}
        attributi_attuali = {(farmaco.nome) for farmaco in listafarmaci}

        assert attributi_oracolo == attributi_attuali





