from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://www.saucedemo.com/?utm_source=chatgpt.com")

driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')

driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')

driver.find_element(By.XPATH,'//*[@id="login-button"]').click()

all_a = driver.find_elements(By.TAG_NAME, 'a')

print("all links with anker tag :" , len(all_a))

for link in all_a: print(link.text)

time.sleep(5)
driver.quit()