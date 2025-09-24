from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcMainPage:
    """
    Page Object для калькулятора на сайте bonigarcia.dev.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver экземпляр браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку выполнения операций.

        :param delay: Задержка в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        :param button: Текст кнопки.
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']"
        ).click()

    def click_buttons(self, buttons: list[str]) -> None:
        """
        Последовательно нажимает на список кнопок.

        :param buttons: Список текстов кнопок.
        """
        for button in buttons:
            self.click_button(button)

    def wait_for_result(self, expected_result: str, delay: int) -> None:
        """
        Ожидает появления результата на экране.

        :param expected_result: Ожидаемый результат.
        :param delay: Задержка в секундах.
        """
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result
            )
        )

    def get_result(self) -> str:
        """
        Получает текст результата с экрана калькулятора.

        :return: Результат вычислений.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
