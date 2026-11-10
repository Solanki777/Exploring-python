from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/")
# driver.get("https://www.amazon.in/")
# driver.back()
# driver.forward()
# driver.refresh()
# time.sleep(2)

# # links 
# links = driver.find_elements(By.XPATH,
#     '//*[@id="navbar-main"]//a'
# )
# print(len(links))

# links[0].click()

# # links : it only returns first link in web bage 
# # links = driver.find_element(By.XPATH,
# #     '//*[@id="navbar-main"]//a'
# # )

# # print(links)



driver.get("https://admin-demo.nopcommerce.com/login")

wait = WebDriverWait(driver, 60)

wait.until(
    lambda d: (
        "Performing security verification" not in d.page_source
        and "Just a moment" not in d.title
    )
)

print("Verification page finished")
time.sleep(4)
driver.clear()
em = driver.find_element(By.XPATH,'//*[@id="Email"]')
em.send_keys("as@gmail.com")

# it will print balnk becuase of there is nothing inside the tag for input tag we know that in html there is no text between 
print(em.text)

# but this is used for the values written inside the input box 
print(em.get_attribute('value'))