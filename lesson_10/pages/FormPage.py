from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Класс страницы формы.
    """

    def __init__(self, driver):
        """
        Инициализация страницы формы.

        :param driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открыть страницу формы")
    def open(self) -> None:
        """Открывает страницу формы."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.step("Заполнить все поля формы")
    def fill_form(self) -> None:
        """Заполняет поля формы данными из словаря self.fields."""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located(
                    (By.NAME, field))).send_keys(value)

    @allure.step("Отправить форму")
    def submit_form(self) -> None:
        """Нажимает кнопку Submit для отправки формы."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получить класс элемента поля: {field_id}")
    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает класс поля по ID.

        :param field_id: ID поля формы
        :return: строка с классом элемента
        """
        element = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверка ошибки в поле ZIP Code")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет, есть ли ошибка в поле ZIP Code.

        :return: True если есть класс alert-danger, иначе False
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка успешного заполнения всех обязательных полей")
    def check_fields_success(self) -> bool:
        """
        Проверяет, что все обязательные поля заполнены корректно.

        :return: True если все поля содержат класс 'success', иначе False
        """
        fields = [
            'first-name', 'last-name', 'address', 'e-mail',
            'phone', 'city', 'country', 'job-position', 'company'
            ]
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка успешной отправки формы")
    def check_form_submission(self) -> None:
        """
        Проверяет успешную отправку формы.

        :raises AssertionError: если есть ошибка в ZIP или не все поля успешны
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
