from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def open(self):
        self.driver.get("https://www.google.com/")

    def search(self, text):
        box = self.driver.find_element(*self.search_box)
        box.clear()
        box.send_keys(text + "\n")

    def get_results(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        results = self.driver.find_elements(
            By.CSS_SELECTOR, "div.tF2Cxc, div.g, div.MjjYud")
        return results
