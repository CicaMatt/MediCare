import unittest
from urllib.parse import quote

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskDir import app, Test

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('querty')}@localhost:3306/testmedicare"


@pytest.fixture
def client(config):
    app.config.update({config: True})
    with app.test_client() as client:
        yield client

    def setUp(self):
        self.app = self.client(config_name='TESTING')
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Crea il database in memoria
        db.create_all()

        # Alcuni dati di esempio per il testing
        self.sample_data = {
            'campo1': 'valore1',
            'campo2': 'valore2',
            # ... aggiungi i campi necessari per il tuo metodo ...
        }

        def tearDown(self):
            # Elimina il database e chiudi l'app
            self.db.session.remove()
            self.db.drop_all()
            self.app_context.pop()

        def testGet