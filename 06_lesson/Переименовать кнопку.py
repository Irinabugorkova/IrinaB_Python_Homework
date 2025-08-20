from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager
                                                ().install()))

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.ID, "newButtonName")
element.clear()

element.send_keys("SkyPro")

wait = WebDriverWait(driver, 4)

button = driver.find_element(By.ID, "updatingButton").click()
button_text = wait.until(
    EC.text_to_be_present_in_element(
        (By.ID, "updatingButton"), "SkyPro"
    )
)

updated_button = driver.find_element(By.ID, "updatingButton")
print(updated_button.text)

driver.quit()
