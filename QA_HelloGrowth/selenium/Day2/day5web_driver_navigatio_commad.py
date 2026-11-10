from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.get("https://www.amazon.in/")
driver.back()
driver.forward()
driver.refresh()
time.sleep(2)

# links 
links = driver.find_elements(By.XPATH,
    '//*[@id="navbar-main"]//a'
)
print(len(links))

# links : it only returns first link in web bage 
links = driver.find_element(By.XPATH,
    '//*[@id="navbar-main"]//a'
)

print(links)

driver.quit()
