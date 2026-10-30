from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")

driver.find_element(By.ID,"email").send_keys("hello")
print("The values in enters")
driver.find_element(By.XPATH,"//a[@href='Register.html']").click()
driver.close()
print("crome is Closed")