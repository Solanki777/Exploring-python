from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys("selenium")

driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()

link_tags = driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']//a")

print("Links found:", len(link_tags))
main = driver.current_window_handle
for link in link_tags:
    url = link.get_attribute("href")
    driver.switch_to.new_window("tab")
    driver.get(url)
    
    

windows = driver.window_handles
print(len(windows))
print("Links found:", len(link_tags))
time.sleep(5)

driver.close()


