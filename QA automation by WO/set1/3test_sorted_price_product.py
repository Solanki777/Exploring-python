from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


ops = webdriver.ChromeOptions()

ops.add_argument("--disable-features=PasswordManagerOnboarding")


driver = webdriver.Chrome(options=ops)
driver.maximize_window()

try :
    wait = WebDriverWait(driver,10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    headding = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    assert headding.text == "Products"
    print("Pass1") 

    dropdown = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select')

    sort = Select(dropdown)
    sort.select_by_index(2)
    time.sleep(3)

    # Locate dropdown again
    dropdown = driver.find_element(
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div/span/select'
    )

    sort = Select(dropdown)

    assert sort.first_selected_option.text == "Price (low to high)"
    print("pass2")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    all_p = []


    for price in prices:
        all_p.append(float(price.text.replace("$", "")))

    assert all_p == sorted(all_p)
    print("pass3")

    
except Exception as e :
    print("test case faild ",e)