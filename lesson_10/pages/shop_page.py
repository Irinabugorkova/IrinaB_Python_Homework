from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """
    Класс страницы авторизации магазина.
    """
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver экземпляр браузера
        """
        self.driver = driver

    @allure.step("Открыть страницу логина")
    def open(self) -> None:
        """Открывает страницу авторизации магазина."""
        self.driver.get(self.URL)

    @allure.step("Войти в систему с логином '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Авторизация пользователя.

        :param username: имя пользователя
        :param password: пароль
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    """
    Класс страницы товаров магазина.
    """

    def __init__(self, driver):
        """
        Инициализация страницы товаров.

        :param driver: WebDriver экземпляр браузера
        """
        self.driver = driver

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию.

        :param product_name: название товара
        """
        locator = (
            By.XPATH, f"//div[text()='{
                product_name}']/ancestor::div[@class='inventory_item']//button"
                )
        self.driver.find_element(*locator).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    """
    Класс страницы корзины.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver экземпляр браузера
        """
        self.driver = driver

    @allure.step("Перейти к оформлению заказа (Checkout)")
    def checkout(self) -> None:
        """Нажимает кнопку Checkout."""
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    """
    Класс страницы оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация страницы Checkout.

        :param driver: WebDriver экземпляр браузера
        """
        self.driver = driver

    @allure.step("Заполнить форму Checkout")
    def fill_form(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму Checkout и нажимает Continue.

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: строка с общей суммой
        """
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
