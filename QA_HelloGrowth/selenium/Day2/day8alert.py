from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://qaautomationlabs.com/testing/javaScript-alert.php")

driver.maximize_window()

OK_elert = driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/section/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/button")
OK_c_elert = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/section/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/button")
print_elert = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/section/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/button")

# Ok alert 
# time.sleep(2)
# OK_elert.click()
# time.sleep(2)
# alertwindow = driver.switch_to.alert
# alertwindow.accept()
# time.sleep(2)
# print("simple OK alert")

# Ok and cacel alert
# time.sleep(2)
# OK_c_elert.click()
# alertwindow = driver.switch_to.alert
# alertwindow.accept()
# # alertwindow.dismiss()
# time.sleep(2)
# print("Ok cacel is working fine")

# print pop 
time.sleep(2)
print_elert.click()
alertwindow = driver.switch_to.alert
alertwindow.send_keys("yes we can access the window")
time.sleep(2)
alertwindow.accept()
# alertwindow.dismiss()
print("its working")




driver.close()



