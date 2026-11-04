from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

# absolute xpath / FUll xpath
# driver.find_element(By.XPATH,"/html/body/section[1]/div/input").send_keys("t-shirt")

# partial/relative  xpath
# driver.find_element(By.XPATH,"//*[@id=\"search_product\"]").send_keys("hello")
# driver.find_element(By.XPATH,"//button[@id=\"input_button\"]").click()

# use \ to tell " is the property of find element so do not use it like do not print it. it is in use  

# OR 
# driver.find_element(By.XPATH, """//*[@id="search_product"]""").send_keys("hello")


# or : when you are using the double qutes inside the string then make sure to use single quotes outside 
# 1 . when you are using realative and fulll xpath use | as or two combine two diffrenet xpath
# print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input | /html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input' ))

# # 2.when you are use same kind of x path use or 
# print(driver.find_element(By.XPATH, "//input[@name='username' or @placeholder='Username']"))


# The same way you can use and operator as or 

# starts-with() and contains() operator 



time.sleep(3)

driver.quit()