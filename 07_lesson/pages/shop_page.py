from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name: str):
        locator = (By.XPATH,
                   f"//div[text()='{product_name}']"
                   "/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
