from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()
time.sleep(3)

# self 
# first rech out the element and make it self it the element is the self
capture = driver.find_element(By.XPATH,"//a[contains(text(),'HDFC Life Insurance')]/self::a").text
print(capture)



driver.close()