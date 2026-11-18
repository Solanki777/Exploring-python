from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys("selenium")

driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()

time.sleep(7)
link_tags = driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']//a")

print(len(link_tags))

main_window = driver.current_window_handle
# store the urls 
urls = []

for link in link_tags:
    url = link.get_attribute("href")
    urls.append(url)

for url in urls:
    driver.switch_to.new_window('tab')
    driver.get(url)
    
    
    

windows = driver.window_handles
print(len(windows))
print("Links found:", len(link_tags))
time.sleep(5)


for i in range(len(windows)):
    if i == 0 : 
        print("parent window is clossing ..")
        driver.switch_to.window(windows[i])
        driver.close()
    else :

        driver.switch_to.window(windows[i])
        print(driver.title)
        if driver.title == "Selenium in biology - Wikipedia": driver.close()
    

driver.switch_to.window(windows[4])
driver.close()
time.sleep(3)
driver.quit()

    



