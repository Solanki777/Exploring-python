from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

loginbtn = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")

print("login button is selcted ? " ,loginbtn.is_selected())

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")

time.sleep(3)

loginbtn = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

# check the particular element is displyed in the webpage or not 
print("login button is displyed or not ? " ,loginbtn.is_displayed())
print("login button is selcted ? " ,loginbtn.is_selected())


loginbtn = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

# ready to interact or not
print("login button is intractable or not " ,loginbtn.is_enabled())

logo = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[1]/img')


print("logo element is interactable " ,logo.is_enabled())
print("logo is selected " ,logo.is_selected())


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(4)


# switch tab 
driver.switch_to.new_window('tab')
driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(2)


# close the orageHRM tab 
tabs = driver.window_handles
driver.switch_to.window(tabs[0])
driver.close()

driver.switch_to.window(tabs[1])

time.sleep(3)

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")

print("Before clicking:", checkbox.is_selected())

checkbox.click()

print("After clicking:", checkbox.is_selected())

# close all website
driver.quit()