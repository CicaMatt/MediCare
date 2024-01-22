import bcrypt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app, db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import database_exists
from flaskDir.MediCare.model.entity import Medici


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}

        with app.app_context():
            password = "123password"
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            password = hashed
            medico = Medici.Medico()
            medico.nome = "Pippo"
            medico.cognome = "Tavolino"
            medico.email = "pippo@gmail.com"
            medico.password_hash = password
            medico.città = "Piccola Svizzera"
            medico.specializzazione = "Chirurigia"
            medico.tariffa = 50
            medico.iscrizione_albo = 12345

            db.session.add(medico)
            db.session.commit()

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                db.session.delete(Medici.Medico.query.filter_by(email="pippo@gmail.com").first())
                db.session.commit()

    def test_loginusernotregistered(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1920, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "doc").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("paperino@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("pipposultavolino")
        self.driver.find_element(By.ID, "invio").click()

    def test_login_failedforemail(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "doc").click()
        self.driver.find_element(By.ID, "email").send_keys("pippi@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("123password")
        self.driver.find_element(By.ID, "invio").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "errore")))
        msg_content = self.driver.find_element(By.ID, "errore").text
        assert "Credenziali fornite errate" == msg_content

    def test_login_failedforpassword(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "doc").click()
        self.driver.find_element(By.ID, "email").send_keys("pippo@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "invio").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "errore")))
        msg_content = self.driver.find_element(By.ID, "errore").text
        assert "Credenziali fornite errate" == msg_content

    def test_login_success(self):
        self.driver.get("http://127.0.0.1:5000")
        self.driver.set_window_size(1920, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "doc").click()
        self.driver.find_element(By.ID, "email").send_keys("pippo@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("123password")
        self.driver.find_element(By.ID, "invio").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "medico")))
        msg_content = self.driver.find_element(By.ID, "medico").text
        assert "Salve dottore" == msg_content
