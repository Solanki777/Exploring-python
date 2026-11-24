from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

print("checkbox 1 status",driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]').is_selected())
before1 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]').is_selected()
print("checkbox 2 status",driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]').is_selected())
before2 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]').is_selected()


driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]').click()
driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]').click()


print("checkbox 1 status",driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]').is_selected())
after1 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]').is_selected()
print("checkbox 2 status",driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]').is_selected())
after2 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]').is_selected()

driver.close()

assert before1 != before2 and after1 != after2