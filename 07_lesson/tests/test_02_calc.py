import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc_sum(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.press_number(7)
    calc_page.press_operator("+")
    calc_page.press_number(8)
    calc_page.press_equal()

    result = calc_page.get_result(expected="15")
    assert result == "15", f"Expected 15, but got {result}"
