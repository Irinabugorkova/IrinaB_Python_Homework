import pytest
import allure
from selenium import webdriver
from pages.CalcMainPage import CalcMainPage
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора")
@allure.description("Тестирует калькулятор с задержкой и проверяет результат.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "÷", "2", "4", 5),
    ],
)
def test_calculator_flow(
    driver, num1: str, operation: str, num2: str,
    expected_result: str, delay: int
) -> None:
    with allure.step("Открытие страницы калькулятора"):
        main_page = CalcMainPage(driver)
        main_page.open()

    with allure.step(f"Установка задержки: {delay} секунд"):
        main_page.set_delay(delay)

    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, ="):
        main_page.click_buttons([num1, operation, num2, "="])

    with allure.step("Ожидание результата"):
        main_page.wait_for_result(expected_result, delay)

    with allure.step("Проверка результата"):
        actual_result = main_page.get_result()
        assert actual_result == expected_result, (
            f"Ожидалось: {expected_result}, получено: {actual_result}"
        )
