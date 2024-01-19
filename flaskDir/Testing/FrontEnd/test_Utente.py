import bcrypt
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app,db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import database_exists
from flaskDir.MediCare.model.entity import Paziente
from flaskDir.MediCare.model.entity import DocumentoSanitario

class TestFascicolo():
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars={}
        self.driver.implicitly_wait(10)


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
        self.driver.set_window_size(1920,1080)
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
                db.session.delete(Paziente.Paziente.query.filter_by(CF="CSBGNN2103456VBM").first())
                db.session.commit()



    def test_ISEEneg(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1934, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"paziente")))
        self.driver.find_element(By.ID, "paziente").click()
        self.driver.find_element(By.CSS_SELECTOR, ".px-4:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "Modifica").click()
        self.driver.find_element(By.ID, "isee").click()
        self.driver.find_element(By.ID, "isee").send_keys("-20000")
        self.driver.find_element(By.ID, "isee").send_keys(Keys.ENTER)
        element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"ISEE")))
        assert element.text == "€10000.00"

    def test_ISEEValid(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1934, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "paziente")))
        self.driver.find_element(By.ID, "paziente").click()
        self.driver.find_element(By.CSS_SELECTOR, ".px-4:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "Modifica").click()
        self.driver.find_element(By.ID, "isee").click()
        self.driver.find_element(By.ID, "isee").send_keys("20000")
        self.driver.find_element(By.ID, "isee").send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ISEE")))
        assert element.text == "€20000.00"