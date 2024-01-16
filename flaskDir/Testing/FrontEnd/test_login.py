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

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                db.session.delete(Paziente.Paziente.query.filter_by(CF="CSBGNN2103456VBM").first())
                db.session.commit()


    def test_loginUserNotRegistered(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1920,1080)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("paperino@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("pipposultavolino")
        self.driver.find_element(By.ID, "invio").click()

    def test_login_failedForEmail(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920,1080)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID,"user").click()
        self.driver.find_element(By.ID,"email").send_keys("pippi@gmail.com")
        self.driver.find_element(By.ID,"password").send_keys("123password")
        self.driver.find_element(By.ID,"invio").click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"errore")))
        msg_content=self.driver.find_element(By.ID,"errore").text
        assert "Credenziali fornite errate" == msg_content

    def test_login_failedForPassword(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920,1080)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID,"user").click()
        self.driver.find_element(By.ID,"email").send_keys("pippo@gmail.com")
        self.driver.find_element(By.ID,"password").send_keys("password")
        self.driver.find_element(By.ID,"invio").click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"errore")))
        msg_content=self.driver.find_element(By.ID,"errore").text
        assert "Credenziali fornite errate" == msg_content

    def test_login_success(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920,1080)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID,"user").click()
        self.driver.find_element(By.ID,"email").send_keys("pippo@gmail.com")
        self.driver.find_element(By.ID,"password").send_keys("123password")
        self.driver.find_element(By.ID,"invio").click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"paziente")))
        msg_content=self.driver.find_element(By.ID,"paziente").text
        assert "Ciao, Pippo" == msg_content



