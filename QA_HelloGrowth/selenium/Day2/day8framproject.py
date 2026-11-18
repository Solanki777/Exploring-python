from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://qa.randomly.online/practice/frames?utm_source=chatgpt.com")

driver.maximize_window()
code = driver.find_element(By.XPATH, '//*[@id="access-code"]').text

print("code : ",code)
print("type :",type(code))


frem = driver.find_element(By.XPATH,'//*[@id="practice-iframe"]')

driver.switch_to.frame(frem)

print("in frame : " , driver.find_element(By.XPATH,'/html/body/p[1]/strong').text)

driver.find_element(By.XPATH,'//*[@id="frame-input"]').send_keys(code)

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="frame-submit"]').click()

print("result : " ,driver.find_element(By.XPATH,'//*[@id="frame-status"]').text)


print("we goingin thorugh it")


driver.switch_to.default_content()


driver.quit()