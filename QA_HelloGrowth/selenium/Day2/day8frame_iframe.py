from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# frame is those element which is used implement othere website into your 
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")

# count frames 
frame = driver.find_elements(By.TAG_NAME,"iframe")

print("total iframes :" ,len(frame))

driver.switch_to.frame(0)

print(driver.find_element(By.TAG_NAME,"h1").text)

driver.switch_to.default_content()

print("back to main page ")

driver.close()

