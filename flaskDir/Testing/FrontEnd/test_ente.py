from telnetlib import EC

import bcrypt
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy_utils import  database_exists
from flaskDir.MediCare.model.entity import  EnteSanitario
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico


class TestAddMedico():
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}
        self.is_second_test = False

        with app.app_context():
            password = "123password"
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            password = hashed
            ente = EnteSanitario()
            ente.nome = 'Sanità'
            ente.email = 'domenico@gmail.com'
            ente.password_hash = password
            ente.città = 'Avellino'
            db.session.add(ente)
            db.session.commit()

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                if self.is_second_test:
                    db.session.delete(Medico.query.filter_by(email="domenicourciuoli20@gmail.com").first())

                db.session.delete(EnteSanitario.query.filter_by(email="domenico@gmail.com").first())
                db.session.commit()

    def test_addMedico(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1046, 766)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Accedi come Ente").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("domenico@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123password")
        self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
        self.driver.find_element(By.LINK_TEXT, "Ciao, Sanità").click()
        self.driver.find_element(By.ID, "open-modal").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("domenicourciuoli20@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.NAME, "reparto").click()
        self.driver.find_element(By.NAME, "reparto").send_keys("Cardiologia")
        self.driver.find_element(By.CSS_SELECTOR, ".md\\3Amb-0:nth-child(2)").click()
        self.driver.find_element(By.NAME, "specializzazione").click()
        self.driver.find_element(By.NAME, "specializzazione").send_keys("chirurgia")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-red-600").click()

    def test_failaddmedico(self):  # e-mail medico già esistente
        self.is_second_test = True
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1048, 768)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Accedi come Ente").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("domenico@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123password")
        self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
        self.driver.find_element(By.LINK_TEXT, "Ciao, Sanità").click()
        self.driver.find_element(By.ID, "open-modal").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("domenicourciuoli20@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.NAME, "reparto").click()
        self.driver.find_element(By.NAME, "reparto").send_keys("Cardiologia")
        self.driver.find_element(By.CSS_SELECTOR, ".md\\3Amb-0:nth-child(2)").click()
        self.driver.find_element(By.NAME, "specializzazione").click()
        self.driver.find_element(By.NAME, "specializzazione").send_keys("chirurgia")
        self.driver.find_element(By.CSS_SELECTOR, ".bg-red-600").click()
