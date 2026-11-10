from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.get("https://affiliate-program.amazon.in/app/onboarding/checklist")
driver.back()
driver.forward()
driver.refresh()

driver.quit()
