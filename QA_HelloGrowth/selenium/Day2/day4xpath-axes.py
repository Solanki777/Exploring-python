from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()
time.sleep(3)

# self 
# first rech out the element and make it self it the element is the self
# capture = driver.find_element(By.XPATH,"//a[contains(text(),'HDFC Life Insurance')]/self::a").text
# print(capture)

# parent : here parent td as nothing inside the td element so defaultly it will print the self tag inner text
# capture_p = driver.find_element(By.XPATH,"//a[contains(text(),'HDFC Life Insurance')]/parent::td").text
# print(capture_p) 

# ancestor which give the gradparent address
# capture_p = driver.find_elements(By.XPATH,"//a[contains(text(),'HDFC Life Insurance')]/ancestor::tr/child::td")
# print(len(capture_p))

# following sibling
# capture_p = driver.find_element(By.XPATH,"//a[contains(text(),'HDFC Life Insurance')]/parent::td/following-sibling::td").text
# print(capture_p)



driver.close()