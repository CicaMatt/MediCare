
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app, db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import database_exists
from flaskDir.MediCare.model.entity import Paziente, Medici
from flaskDir.source.autenticazione import AutenticazioneService


class TestRegistrazione:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                db.session.delete(Medici.Medico.query.filter_by(email="testmedico@example.com").first())
                db.session.commit()

    def test_registrazione(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1200, 760)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.CSS_SELECTOR, "#doc > .d-block").click()
        self.driver.find_element(By.LINK_TEXT, "Crea Account").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("testmedico@example.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "nome").click()
        self.driver.find_element(By.ID, "nome").send_keys("Medico")
        self.driver.find_element(By.ID, "cognome").click()
        self.driver.find_element(By.ID, "cognome").send_keys("Dottore")
        self.driver.find_element(By.ID, "code").click()
        self.driver.find_element(By.ID, "code").send_keys("1234567")
        self.driver.find_element(By.ID, "specializzazione").click()
        dropdown = self.driver.find_element(By.ID, "specializzazione")
        dropdown.find_element(By.XPATH, "//option[. = 'Oculistica']").click()
        self.driver.find_element(By.ID, "citta").click()
        self.driver.find_element(By.ID, "citta").send_keys("Napoli")
        self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
        with app.app_context():
            assert Medici.Medico.query.filter_by(email="testmedico@example.com").first()