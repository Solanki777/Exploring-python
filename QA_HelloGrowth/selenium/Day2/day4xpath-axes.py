from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()
time.sleep(3)
driver.close()