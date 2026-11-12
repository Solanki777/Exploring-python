from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.implicitly_wait(10)

googletext = driver.find_element(By.ID,'ti6dpd')


googletext.send_keys("selenium")

googletext.submit()

wait = WebDriverWait(driver,120)

if "sorry" in driver.current_url:
    print("captch detectd")
    print("please complete the it")

    wait.until(
        lambda d: "sorry" not in d.current_url
    )
print("continue automation ....")

driver.quit()