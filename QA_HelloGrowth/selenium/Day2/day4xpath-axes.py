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

# preceding-sibling
# capture = driver.find_element(By.XPATH ,"//td[contains(text(),'563.65')]/preceding-sibling::td").text
# print(capture)


# preceding
# capture_t = driver.find_elements(By.XPATH ,"//td[contains(text(),'563.65')]/preceding::tr")
# print(len(capture_t))

# # following
# capture = driver.find_elements(By.XPATH ,"//td[contains(text(),'563.65')]/following::tr")
# print(len(capture))

# # total tr of td is :
# total_tr = len(capture_t) + len(capture) + 1 #current
# print(total_tr)

# descendant
capture = driver.find_elements(By.XPATH,"//td[contains(text(),'563.65')]/parent::tr/parent::tbody/descendant::tr")
print(len(capture))

driver.close()