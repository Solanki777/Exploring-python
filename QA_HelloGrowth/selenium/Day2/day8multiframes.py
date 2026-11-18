from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()

# first locate the ifram 
frem = driver.find_element(By.XPATH,'//*[@id="singleframe"]')
print("element found")

driver.switch_to.frame(frem)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("hello world")

driver.switch_to.default_content()

print("getting back to normal")

driver.close()
# https://www.selenium.dev/selenium/docs/api/java/index.html?utm_source=chatgpt.com

