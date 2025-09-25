import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    Содержит методы для управления калькулятором: ввод задержки,
    нажатие кнопок и получение результата.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку выполнения операций.

        :param seconds: время задержки в секундах
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажать цифру {number}")
    def press_number(self, number: int) -> None:
        """
        Нажимает числовую кнопку на калькуляторе.

        :param number: цифра от 0 до 9
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{number}']").click()

    @allure.step("Нажать оператор {operator}")
    def press_operator(self, operator: str) -> None:
        """
        Нажимает кнопку оператора.

        :param operator: оператор ('+', '-', '*', '/')
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{operator}']").click()

    @allure.step("Нажать '='")
    def press_equal(self) -> None:
        """Нажимает кнопку '=' для вычисления результата."""
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Получить результат (ожидаемое значение: {expected})")
    def get_result(self, expected: str = "15", timeout: int = 50) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :param expected: ожидаемое значение результата
        :param timeout: время ожидания результата в секундах
        :return: текст результата
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
