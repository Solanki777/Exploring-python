from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# username access 
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")

# password access  
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")

# click onthe login button
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()

print(driver.title)
if driver.title == "Swag Labs":
    print("Scenario 1 passes")
else :
    print("Scenario 1 Failed")

driver.close()
