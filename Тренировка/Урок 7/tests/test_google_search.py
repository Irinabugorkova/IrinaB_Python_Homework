import pytest
from selenium import webdriver
from pages.google_page import GooglePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_google_search(driver):
    page = GooglePage(driver)
    page.open()
    page.search("Selenium Python")
    results = page.get_results()
    assert len(results) > 0, "Нет результатов поиска"
