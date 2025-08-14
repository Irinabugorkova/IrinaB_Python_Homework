from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)

    blue_button = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
    )
    blue_button.click()
    time.sleep(2)

    WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

finally:
    driver.quit()
