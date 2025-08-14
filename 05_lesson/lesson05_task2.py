from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/dynamicid")

    button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()
    time.sleep(3)

finally:
    driver.quit()
