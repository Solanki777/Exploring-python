from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 1.alert 
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")


# driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()

# time.sleep(3)
# alt = driver.switch_to.alert
# alt.accept()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# # main = driver.current_window_handle()


# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()

# time.sleep(3)
# alt = driver.switch_to.alert
# alt.accept()


# 2.ok cancel alert

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()


# time.sleep(2)
# ac = driver.switch_to.alert

# # ac.accept
# # OR 
# ac.dismiss

# time.sleep(3)


# 3.propmt sending 

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

print(driver.title)
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()

time.sleep(2)

alt = driver.switch_to.alert
time.sleep(2)
alt.send_keys("hello world")



# OR 
# ac.dismiss

time.sleep(3)

driver.close()

