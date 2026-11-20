from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# First Name 
driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("Solanki")
time.sleep(2)

# Last name 
driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys("Mahesh")
time.sleep(2)

# mail 
driver.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys("s@gmail.com")
time.sleep(2)

# gender
driver.find_element(By.XPATH,'//*[@id="genterWrapper"]/div[2]/div[1]/label').click()
time.sleep(2)

# mobile 
driver.find_element(By.XPATH,'//*[@id="userNumber"]').send_keys("9725214521")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]').click()

driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div[4]').click()
time.sleep(2)


driver.find_element(By.XPATH,'//*[@id="hobbies-checkbox-1"]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="hobbies-checkbox-2"]').click()
time.sleep(2)

# click
driver.find_element(By.XPATH,'//*[@id="submit"]').click()

time.sleep(8)

if driver.find_element(By.XPATH,'//*[@id="example-modal-sizes-title-lg"]').is_displayed():print("Pass")
else :print("Failed")


driver.close()