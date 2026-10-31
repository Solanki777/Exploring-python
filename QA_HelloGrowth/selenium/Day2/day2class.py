from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.automationpractice.in")
findings = driver.find_elements(By.CLASS_NAME,"qa-uheader")
print(len(findings))