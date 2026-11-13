from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/dynamic.html?utm_source=chatgpt.com")


# wait object which everyt is used to for diffrent pages to be loadded 
wait = WebDriverWait(driver,10)




# EC - excepted condition : it will return the element if it exits in the web page else it trow the exception
gotch_add_box = wait.until(
    EC.visibility_of_element_located((By.ID ,'adder'))
)

gotch_add_box.click()
box_created = wait.until(
    EC.visibility_of_element_located(
        ((By.ID,"box0"))
    )

)

if gotch_add_box : print(f"yes {box_created}")




driver.close()
