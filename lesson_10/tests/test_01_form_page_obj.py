import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.FormPage import FormPage


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для запуска и завершения браузера Chrome.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Тест формы: успешная отправка и проверка полей")
@allure.description(
    "Проверка заполнения формы и успешной отправки с валидацией всех полей")
@allure.feature("FormPage")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open()

    with allure.step("Заполнить форму"):
        form_page.fill_form()

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Проверить отправку формы"):
        form_page.check_form_submission()
