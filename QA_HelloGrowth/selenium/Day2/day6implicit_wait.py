from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(3)

driver.find_element(By.ID,'ti6dpd').send_keys("selenium")

driver.find_element(By.ID,'ti6dpd').submit()

driver.quit()