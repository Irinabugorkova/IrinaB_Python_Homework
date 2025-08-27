import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.XPATH,
                        "//div[text()='Sauce Labs Backpack']/ancestor::div"
                        "[@class='inventory_item']//button").click()
    driver.find_element(By.XPATH,
                        "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div"
                        "[@class='inventory_item']//button").click()
    driver.find_element(By.XPATH,
                        "//div[text()='Sauce Labs Onesie']/ancestor::div"
                        "[@class='inventory_item']//button").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Irina")
    driver.find_element(By.ID, "last-name").send_keys("Bugorkova")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert total == "Total: $58.29"
