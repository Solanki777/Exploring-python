from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://mypage.rediff.com/login/dologin")

driver.maximize_window()

# press login
driver.find_element(By.XPATH,'//*[@id="btnLogin"]').click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
print("entered the captha")

driver.close()