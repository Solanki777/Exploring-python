from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://www.saucedemo.com/?utm_source=chatgpt.com")

driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')

driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')

driver.find_element(By.XPATH,'//*[@id="login-button"]').click()


# this can be done by internal or external links both will be the same 
all_a = driver.find_elements(By.TAG_NAME, 'a')

print("all links with anker tag :" , len(all_a))

for link in all_a: print(link.text)

# broken links 
driver.switch_to.new_window("tab")
driver.get("http://www.deadlinkcity.com/")

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="maintext"]/div[1]/ul/li[1]')))

all_a = driver.find_elements(By.TAG_NAME,'a')

ctn = 0


for link in all_a:
    try :
        url = link.get_attribute('href')
        res = requests.head(url,timeout=10)

        if res.status_code >= 400 : ctn += 1
        print(f"the broken link:{url} - Status : {res.status_code}")
    except requests.exceptions.RequestException as e :print("broken link :{url} Error : {e}")

print("total broken link :" ,ctn)
 
# link's status code greater than 400 are broken links 
print("total links :" , len(all_a))


time.sleep(5)
driver.quit()