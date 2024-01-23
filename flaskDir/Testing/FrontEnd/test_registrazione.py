
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir import app, db
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy_utils import database_exists
from flaskDir.MediCare.model.entity import Paziente


class TestRegistrazione:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            with app.app_context():
                db.session.delete(Paziente.Paziente.query.filter_by(CF="VNTGNN80A01A783Y").first())
                db.session.commit()

    def test_registrazione(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1920, 1080)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pb-6").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Crea Account")))
        self.driver.find_element(By.LINK_TEXT, "Crea Account").click()
        self.driver.find_element(By.ID, "nome").click()
        self.driver.find_element(By.ID, "nome").send_keys("Gennaro")
        self.driver.find_element(By.ID, "cognome").click()
        self.driver.find_element(By.ID, "cognome").send_keys("Ventrone")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("genven@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("testexample")
        self.driver.find_element(By.ID, "code").click()
        self.driver.find_element(By.ID, "code").send_keys("VNTGNN80A01A783Y")
        self.driver.find_element(By.ID, "cellulare").click()
        self.driver.find_element(By.ID, "cellulare").send_keys("3312258345")
        self.driver.find_element(By.ID, "cittanascita").click()
        self.driver.find_element(By.ID, "cittanascita").send_keys("Benevento")
        self.driver.find_element(By.ID, "datanascita").click()
        self.driver.find_element(By.ID, "datanascita").send_keys("2000-12-12")
        self.driver.find_element(By.ID, "domicilio").click()
        self.driver.find_element(By.ID, "domicilio").send_keys("Benevento")
        self.driver.find_element(By.ID, "sesso").click()
        self.driver.find_element(By.ID, "sesso").send_keys("Maschio")
        self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("genven@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("testexample")
        self.driver.find_element(By.ID, "invio").click()
