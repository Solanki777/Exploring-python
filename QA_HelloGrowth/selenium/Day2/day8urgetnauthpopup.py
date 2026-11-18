from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# you click on web and the pop up is come so now you can not directly go into the alert and also apart from it there is multiple input field in asking
# driver.get("https://the-internet.herokuapp.com/basic_auth")

# what you can do is injecting credetials in url 

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.close()


