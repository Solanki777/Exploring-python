from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


# mobile 
driver.find_element(By.XPATH,'//*[@id="userNumber"]').send_keys("4512")
time.sleep(2)

# click
try :
    print(driver.find_element(By.XPATH,'//*[@id="submit"]').click())
    print("test case faild")
except :
    print("test case passed")


driver.close()