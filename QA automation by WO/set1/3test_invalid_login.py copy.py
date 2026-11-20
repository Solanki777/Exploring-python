from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# username access 
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")


# password access  
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")

# click onthe login button
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()



# bypass the fillter 
# onel = driver.switch_to.alert
# onel.accept()



fillter = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select')

fillter.click()

options = Select(fillter)
options.select_by_index(2)
time.sleep(5)

prices = driver.find_element(By.XPATH,'//*[@id="inventory_container"]//text()[2]')
ans = []
for p in prices:
    ans.append(int(p.text))

ans.sort()
if ans[0] == 7.99 : print("test case passed")
else : print("test case faild")




