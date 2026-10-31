from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.automationpractice.in")
findings = driver.find_elements(By.CLASS_NAME,"qa-uheader")
print(len(findings))
print(findings)


findings_tag = driver.find_elements(By.TAG_NAME,"a")
print(len(findings_tag))
print(findings_tag)

driver.quit()
