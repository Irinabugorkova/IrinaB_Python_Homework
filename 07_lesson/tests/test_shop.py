import pytest
from selenium import webdriver
from pages.shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.go_to_cart()

    cart_page.checkout()
    checkout_page.fill_form("Irina", "Bugorkova", "123456")

    total = checkout_page.get_total()

    assert total == "Total: $58.29"
