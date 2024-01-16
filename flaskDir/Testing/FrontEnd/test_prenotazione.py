from telnetlib import EC
import bcrypt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app,db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import create_database, database_exists
from flaskDir.MediCare.model.entity import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.source.prenotazioni.services import PrenotazioneService


class TestEffettuazioneprenotazione():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}

        with app.app_context():
            password="PaSs3word"
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            password=hashed
            paziente=Paziente.Paziente()
            paziente.CF="AAAAAAAAAAAAAAAA"
            paziente.nome="Mario"
            paziente.cognome="Rossi"
            paziente.email="stonks@gmail.com"
            paziente.password_hash=password
            paziente.chiaveSPID=123
            paziente.cellulare="3312345678"
            paziente.domicilio="Italia"
            paziente.dataNascita="2001/01/01"
            paziente.luogoNascita="Salerno"
            paziente.sesso="Maschio"
            paziente.ISEE_ordinario=10000
            db.session.add(paziente)
            db.session.commit()

            self.driver.get("http://127.0.0.1:5000/")
            self.driver.set_window_size(1920, 1080)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"login")))
            self.driver.find_element(By.ID, "login").click()
            self.driver.find_element(By.ID, "user").click()
            self.driver.find_element(By.ID, "email").send_keys("stonks@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("PaSs3word")
            self.driver.find_element(By.ID, "invio").click()

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                prenotazioni = Prenotazione.query.filter_by(pazienteCF="AAAAAAAAAAAAAAAA")
                for prenotazione in prenotazioni:
                    db.session.delete(prenotazione)
                db.session.delete(Paziente.Paziente.query.filter_by(CF="AAAAAAAAAAAAAAAA").first())
                db.session.commit()

    def test_effettua_prenotazione_Success(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.LINK_TEXT, "Prenotazioni").click()
        self.driver.find_element(By.ID, "specialistiche").click()
        self.driver.find_element(By.LINK_TEXT, "Oculistica").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) .flex .text-gray-900").click()
        self.driver.find_element(By.ID, "open-modal30").click()
        self.driver.find_element(By.ID, "open-modal30").click()
        self.driver.find_element(By.ID, "category").click()
        dropdown = self.driver.find_element(By.ID, "category")
        dropdown.find_element(By.XPATH, "//option[. = '17:00']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-red-600").click()
        self.driver.find_element(By.ID, "paziente").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .flex-1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(3) > .px-6 .font-medium").click()

