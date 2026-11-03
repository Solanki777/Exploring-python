from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/products")

driver.maximize_window()

time.sleep(3)

# absolute xpath / FUll xpath
driver.find_element(By.XPATH,"/html/body/section[1]/div/input").send_keys("t-shirt")

time.sleep(3)

driver.quit()