from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/products")

driver.maximize_window()

time.sleep(3)

# absolute xpath / FUll xpath
# driver.find_element(By.XPATH,"/html/body/section[1]/div/input").send_keys("t-shirt")

# partial/relative  xpath
# driver.find_element(By.XPATH,"//*[@id=\"search_product\"]").send_keys("hello")
# driver.find_element(By.XPATH,"//button[@id=\"input_button\"]").click()

# use \ to tell " is the property of find element so do not use it like do not print it. it is in use  

# OR 
# driver.find_element(By.XPATH, """//*[@id="search_product"]""").send_keys("hello")

time.sleep(3)

driver.quit()