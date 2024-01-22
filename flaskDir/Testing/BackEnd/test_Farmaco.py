import pytest
from sqlalchemy_utils import database_exists, create_database
from flaskDir import app, db
from flaskDir.MediCare.model.entity.Farmaco import Farmaco
from flaskDir.source.Farmaci.FarmaciService import FarmaciService


@pytest.fixture(autouse=True, scope='session')
def setup(request):
    # Configura il database di test
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:Unisa@localhost:3306/testmedicare"
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


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


# inserisco categoria valida e non inserisco il prezzo
def test_filtrocatalogofarmacinoprezzo(client):
    sciroppo = Farmaco(prezzo=2.50, nome="Tachipirina", descrizione="Sciroppo", immagine="sciroppo.jpg",
                       categoria="Sciroppo")
    with app.app_context():
        db.session.add(sciroppo)
        db.session.commit()
        categoria = "Sciroppo"
        prezzo = 0

        listafarmaci = list(FarmaciService.filtraCatalogo(categoria, prezzo))

        # Controllo che tutti i farmaci risultanti abbiano le caratteristiche scelte
        assert all(farmaco.categoria == categoria for farmaco in listafarmaci)

        # Controllo che i farmaci risultanti siano uguali all'oracolo
        oracolo = Farmaco.query.filter_by(categoria=categoria).all()
        attributi_oracolo = {farmaco.nome for farmaco in oracolo}
        attributi_attuali = {farmaco.nome for farmaco in listafarmaci}

        assert attributi_oracolo == attributi_attuali

        db.session.delete(sciroppo)
        db.session.commit()


# inserisco categoria non valida e non inserisco il prezzo
def test_filtrocatalogofarmacinoprezzocategoriainvalid(client):
    sciroppo = Farmaco(prezzo=2.50, nome="Tachipirina", descrizione="Sciroppo", immagine="sciroppo.jpg",
                       categoria="Sciroppo")
    with app.app_context():
        db.session.add(sciroppo)
        db.session.commit()
        categoria = "Supposte"
        prezzo = 0

        listafarmaci = list(FarmaciService.filtraCatalogo(categoria, prezzo))

        # Controllo che i farmaci risultanti siano uguali all'oracolo
        oracolo = Farmaco.query.filter_by(categoria=categoria).all()
        attributi_oracolo = {farmaco.nome for farmaco in oracolo}
        attributi_attuali = {farmaco.nome for farmaco in listafarmaci}

        assert attributi_oracolo == attributi_attuali

        db.session.delete(sciroppo)
        db.session.commit()


# inserisco prezzo valido e non inserisco la categoria
def test_filtrocatalogonocat(client):
    compresse = Farmaco(prezzo=3, nome="MomentAct", descrizione="Compresse", immagine="Moment.jpg",
                        categoria="Compresse")
    with app.test_request_context():
        with app.app_context():
            db.session.add(compresse)
            db.session.commit()
            prezzo = 20

            listafarmaci = list(FarmaciService.filtraCatalogo("-", prezzo))

            assert all(farmaco.prezzo <= prezzo for farmaco in listafarmaci)
            oracolo = Farmaco.query.filter(Farmaco.prezzo <= prezzo).all()
            attributi_oracolo = {farmaco.nome for farmaco in oracolo}
            attributi_attuali = {farmaco.nome for farmaco in listafarmaci}

            assert attributi_oracolo == attributi_attuali

            db.session.delete(compresse)
            db.session.commit()


# inserisco prezzo non valido e non inserisco la categoria
def test_filtrocatalogonocatprezzoinvalid(client):
    compresse = Farmaco(prezzo=5, nome="MomentAct", descrizione="Compresse", immagine="Moment.jpg",
                        categoria="Compresse")
    with app.test_request_context():
        with app.app_context():
            db.session.add(compresse)
            db.session.commit()
            prezzo = 2

            listafarmaci = list(FarmaciService.filtraCatalogo("-", prezzo))

            oracolo = Farmaco.query.filter(Farmaco.prezzo <= prezzo).all()
            attributi_oracolo = {farmaco.nome for farmaco in oracolo}
            attributi_attuali = {farmaco.nome for farmaco in listafarmaci}

            assert attributi_oracolo == attributi_attuali

            db.session.delete(compresse)
            db.session.commit()


# non inserisco ne prezzo ne categoria validi
def test_filtrocatalogonoprezzonocategoria(client):
    oki = Farmaco(prezzo=5, nome="OkiTask", descrizione="OkiTask", immagine="Oki.jpg", categoria="Orosolubile")
    with app.test_request_context():
        with app.app_context():
            db.session.add(oki)
            db.session.commit()
            categoria = "Supposte"
            prezzo = 2

            listafarmaci = list(FarmaciService.filtraCatalogo(categoria, prezzo))
            assert not any(farmaco.prezzo == prezzo and farmaco.categoria == categoria for farmaco in listafarmaci)

            db.session.delete(oki)
            db.session.commit()


# inserisco prezzo e categoria validi
def test_filtrocatalogoprezzoecategoria(client):
    oki = Farmaco(prezzo=5, nome="OkiTask", descrizione="OkiTask", immagine="Oki.jpg", categoria="Orosolubile")
    with app.test_request_context():
        with app.app_context():
            db.session.add(oki)
            db.session.commit()
            categoria = "Orosolubile"
            prezzo = 30

            listafarmaci = list(FarmaciService.filtraCatalogo(categoria, prezzo))
            assert all(farmaco.prezzo <= prezzo and farmaco.categoria == categoria for farmaco in listafarmaci)
            oracolo = Farmaco.query.filter(Farmaco.prezzo <= prezzo, Farmaco.categoria == categoria).all()
            attributi_oracolo = {farmaco.nome for farmaco in oracolo}
            attributi_attuali = {farmaco.nome for farmaco in listafarmaci}
            assert attributi_oracolo == attributi_attuali

            db.session.delete(oki)
            db.session.commit()
