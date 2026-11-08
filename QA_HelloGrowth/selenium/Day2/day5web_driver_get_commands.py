from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# get command
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

# title 
print(driver.title)

# current_url
print(driver.current_url)

# page_source
print(driver.page_source)
driver.quit()

