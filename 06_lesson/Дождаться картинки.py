from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 15)
wait.until(EC.invisibility_of_element_located(
    (By.ID, "spinner")
    )
)

images = wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "#image-container img")
        )
)

third_image_src = images[2].get_attribute("src")
print(third_image_src)

driver.quit()
