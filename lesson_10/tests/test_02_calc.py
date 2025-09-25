import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.CalculatorPage import CalculatorPage


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


@allure.title("Тест калькулятора: сложение 7 + 8")
@allure.description(
    "Проверка работы калькулятора с задержкой выполнения операций")
@allure.feature("CalculatorPage")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_sum(driver):
    calc_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Нажать число 7"):
        calc_page.press_number(7)

    with allure.step("Нажать оператор '+'"):
        calc_page.press_operator("+")

    with allure.step("Нажать число 8"):
        calc_page.press_number(8)

    with allure.step("Нажать '='"):
        calc_page.press_equal()

    with allure.step("Получить и проверить результат"):
        result = calc_page.get_result(expected="15")
        assert result == "15", f"Expected 15, but got {result}"
