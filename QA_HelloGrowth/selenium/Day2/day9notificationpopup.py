from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# it contines the functionality of browser
ops = webdriver.ChromeOptions()

ops.add_argument("--disable-notifications")
ops.add_argument("--incognito")
ops.add_argument("--start-maximized")


driver = webdriver.Chrome(options=ops)

driver.get("https://www.youtube.com/")
time.sleep(5)
driver.quit()