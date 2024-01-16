import bcrypt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app,db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import create_database, database_exists
from flaskDir.MediCare.model.entity import Paziente, Medici, EnteSanitario
from flaskDir.MediCare.model.entity.MetodoPagamento import MetodoPagamento


class TestLogin():
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars={}


        with app.app_context():
            password="123password"
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            password=hashed
            paziente=Paziente.Paziente()
            paziente.CF="CSBGNN2103456VBM"
            paziente.nome="Pippo"
            paziente.cognome="Tavolino"
            paziente.email="pippo@gmail.com"
            paziente.password_hash=password
            paziente.chiaveSPID=123
            paziente.cellulare="3312258345"
            paziente.domicilio="Piccola Svizzera"
            paziente.dataNascita="2002/12/12"
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
            self.driver.find_element(By.ID, "email").send_keys("pippo@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("123password")
            self.driver.find_element(By.ID, "invio").click()

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                metodi = MetodoPagamento.query.filter_by(beneficiario="CSBGNN2103456VBM").all()
                for metodo in metodi:
                    db.session.delete(metodo)
                db.session.delete(Paziente.Paziente.query.filter_by(CF="CSBGNN2103456VBM").first())
                db.session.commit()

    def test_addCarta(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1936, 1056)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"paziente")))
        self.driver.find_element(By.ID, "paziente").click()
        self.driver.find_element(By.ID, "open-modal-2").click()
        self.driver.find_element(By.ID, "titolare").click()
        self.driver.find_element(By.ID, "titolare").send_keys("Nome")
        self.driver.find_element(By.ID, "pan").click()
        self.driver.find_element(By.ID, "pan").send_keys("4563767812342345")
        self.driver.find_element(By.ID, "cvv").click()
        self.driver.find_element(By.ID, "cvv").send_keys("435")
        self.driver.find_element(By.ID, "anno").click()
        self.driver.find_element(By.ID, "anno").send_keys("2027")
        self.driver.find_element(By.ID, "mese").click()
        self.driver.find_element(By.ID, "mese").send_keys("01")
        self.driver.find_element(By.CSS_SELECTOR, ".hover\\3A bg-red-500").click()


