from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.maximize_window()

# 1.tag and id selector

# tagname#valueofid
# driver.find_element(By.CSS_SELECTOR,"input#_R_c9l6neappb6amH1_").send_keys("Email add")
# ignore tag you can : valueofid
# driver.find_element(By.CSS_SELECTOR,"#_R_c9l6neappb6amH1_").send_keys("hello")





# driver.close()