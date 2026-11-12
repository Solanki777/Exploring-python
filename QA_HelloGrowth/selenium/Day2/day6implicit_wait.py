from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(3)

googletext = driver.find_element(By.ID,'ti6dpd')


googletext.send_keys("selenium")

googletext.submit()

driver.quit()