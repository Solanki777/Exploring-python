from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://blazedemo.com/")

driver.find_element(By.XPATH,'/html/body/div[3]/form/select[1]').click()


op2 = driver.find_element(By.XPATH,'/html/body/div[3]/form/select[2]').click()

time.sleep(3)

