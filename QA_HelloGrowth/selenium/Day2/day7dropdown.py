from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

# select the select tag because it is the starting of the opetions tag 

select_tag = driver.find_element(By.XPATH,'//*[@id="post-2646"]/div[2]/div/div/div/p/select')

# it will store all options as single object so we have to make it list 
dpdown_el = Select(select_tag)

print(dpdown_el)

# all options as list 
options = dpdown_el.options
for op in options:
    if op.text == 'Zambia' : 
        he = op
        op.click()

if he.is_selected : print("zambia is selected")


#  other way is directly access all options 
# this is one of the xpath : //*[@id="post-2646"]/div[2]/div/div/div/p/select/option[1]

# remove [1] and you got all option 
options = driver.find_elements(By.XPATH,'//*[@id="post-2646"]/div[2]/div/div/div/p/select/option')

for op in options :
    if op.text == "Western Sahara" : 
        ho = op.text 
        op.click()

print(f"now {ho} is selected")
time.sleep()
driver.quit()