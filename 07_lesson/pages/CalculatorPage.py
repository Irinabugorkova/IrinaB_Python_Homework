from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, seconds):

        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_number(self, number):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{number}']").click()

    def press_operator(self, operator):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{operator}']").click()

    def press_equal(self):
        self.driver.find_element(
            By.XPATH, "//span[text()='=']").click()

    def get_result(self, expected="15", timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
