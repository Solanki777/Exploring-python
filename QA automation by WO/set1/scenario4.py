from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# username access 
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")

# password access  
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")

# click onthe login button
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()

driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()

driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

count = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a/span')

if count.text == "2" : 
    print("2 is printed")
else : 
    print("test failed")

time.sleep(4)
driver.find_element(By.XPATH,'//*//*[@id="remove-sauce-labs-backpack"]').click()






if count.text == "1": print('scenario4 passed')
else : print("scenario4 faild")

driver.close()