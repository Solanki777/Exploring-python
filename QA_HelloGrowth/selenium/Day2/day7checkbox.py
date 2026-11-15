from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Chrome()

dr.get("https://testautomationpractice.blogspot.com")

dr.maximize_window()

# select one checkbox
dr.find_element(By.XPATH,'//*[@id="post-body-1307673142697428135"]/div[4]/div[1]/label').click()

# select all 
days = dr.find_elements(By.XPATH,'//input[@type = "checkbox" and contains(@id,"day")]')

for day in days: day.click()

# specific day 
for day in days:
    if day.get_attribute("value") == "sunday": day.click()

# unslect last two 
total_days = len(days)
for l in range(total_days - 2 , total_days) : days[l].click()

# unselect first 2 
for f in range(total_days):
    if f < 2 :
        days[f].click()

# clear all the checkbox
for a in range(total_days):
    if days[a].is_selected() : days[a].click()

time.sleep(4)
dr.close()
