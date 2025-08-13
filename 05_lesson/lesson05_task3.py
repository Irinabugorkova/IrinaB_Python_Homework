from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    input_field.send_keys("Sky")
    time.sleep(2)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("Pro")
    time.sleep(2)

finally:
    driver.quit()
