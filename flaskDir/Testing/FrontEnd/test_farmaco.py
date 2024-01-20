from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from flaskDir.MediCare.model.entity.Farmaco import Farmaco
import time

from flaskDir import app, db


class TestFarmaco():
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}

        with app.app_context():
            farmaco=Farmaco(ID=10, prezzo=5.50, nome="Augmentin", categoria="Compresse", descrizione="Antibiotico per l'influenza alta", immagine="testing.png")
            db.session.add(farmaco)
            db.session.commit()

    def teardown_method(self):
        self.driver.quit()
        with app.app_context():
            db.session.delete(Farmaco.query.filter_by(ID=10).first())
            db.session.commit()



    def test_perCategoria(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1172, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        self.driver.find_element(By.ID, "manufacturer").click()
        dropdown = self.driver.find_element(By.ID, "manufacturer")
        dropdown.find_element(By.XPATH, "//option[. = 'Sciroppo']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-600").click()


    def test_perPrezzo(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1172, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "prezzo").send_keys("9")
        self.driver.find_element(By.ID, "prezzo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-600").click()


    def test_perCategoriaePrezzo(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1172, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        self.driver.find_element(By.ID, "manufacturer").click()
        dropdown = self.driver.find_element(By.ID, "manufacturer")
        dropdown.find_element(By.XPATH, "//option[. = 'Sciroppo']").click()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "prezzo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "prezzo").send_keys("13")
        self.driver.find_element(By.ID, "prezzo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-600").click()


    def test_farmacoNoFindCategoria(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1172, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        self.driver.find_element(By.ID, "manufacturer").click()
        dropdown = self.driver.find_element(By.ID, "manufacturer")
        dropdown.find_element(By.XPATH, "//option[. = 'Supposte']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-600").click()

        error=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"noPresent")))
        assert error
        assert error.text=="Sembra non ci siano farmaci idonei"


    def test_farmacoNoFind(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1920, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.ID, "search").send_keys("benactiveGola")
        self.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)
        error = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "noPresent")))
        assert error
        assert error.text == "Sembra non ci siano farmaci idonei"

    def test_farmacoFind(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1920, 1032)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Farmaci")))
        self.driver.find_element(By.LINK_TEXT, "Farmaci").click()
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.ID, "search").send_keys("Augmentin")
        self.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".h-48").click()
        farmaco = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "nomeFarmaco")))
        assert self.driver.current_url == "http://127.0.0.1:5000/farmacia/dettagliFarmaco?id=10&categoria=Compresse"
        assert farmaco
        assert farmaco.text == "Augmentin"

