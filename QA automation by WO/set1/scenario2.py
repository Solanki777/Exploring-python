from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# username access 
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("invalid")

# password access  
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("invalid")

# click onthe login button
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()


text_tag = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

if text_tag :
    print(text_tag.text)
else : print("scenario 2 Fail")

driver.close()