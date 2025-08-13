from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    time.sleep(1)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(2)

    message = driver.find_element(By.ID, "flash").text
    print(message.split("×")[0].strip())

finally:
    driver.quit()
