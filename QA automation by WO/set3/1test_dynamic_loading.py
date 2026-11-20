from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.XPATH,'//*[@id="start"]/button').click()

wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="finish"]/h4')))

print(
    driver.find_element(By.XPATH,'//*[@id="finish"]/h4').text
)

driver.close()

