import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для запуска и завершения браузера Firefox.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@allure.title("Тест магазина: проверка итоговой суммы корзины")
@allure.description(
    "Логин, добавление товаров в корзину, оформление заказа и проверка суммы")
@allure.feature("ShopPage")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу логина и авторизоваться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")

    with allure.step("Перейти в корзину и оформить заказ"):
        inventory_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_form("Irina", "Bugorkova", "123456")

    with allure.step("Проверить итоговую сумму"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29"
