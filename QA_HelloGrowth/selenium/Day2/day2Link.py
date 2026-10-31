from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")

driver.find_element(By.ID,"email").send_keys("hello")

driver.find_element()



print("The values in enters")


# a tag 

# 1 .  driver.find_element(By.XPATH,"//a[@href='Register.html']").click()


#  2 . OR using css selector 
# driver.find_element(By.CSS_SELECTOR,"a[href='Register.html']").click()


#  3. Or using img tag 
driver.find_element(By.ID, "enterimg").click()

# # 4. if linktext is there 
# driver.find_element(By.LINK_TEXT,"link test").click()

# # or some part of linktext
# driver.find_element(By.PARTIAL_LINK_TEXT,"test").click()




driver.close()
print("crome is Closed")