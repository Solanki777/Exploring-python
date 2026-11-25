from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
wait = WebDriverWait(driver,10)

try :
    first = wait.until(EC.visibility_of_element_located((By.ID,"firstName")))
    first.send_keys("Solanki")
    driver.find_element(By.ID,'lastName').send_keys("Mahesh")

    

except Exception as e:
    print(e)

finally : driver.quit()