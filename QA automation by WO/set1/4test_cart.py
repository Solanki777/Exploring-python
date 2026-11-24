from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,

# it will give the mixture path 
sc_path = os.path.join(os.path.dirname(__file__),"..","screenshots")

# it converts mixture path into absoute path 
sc_path = os.path.abspath(sc_path)




ops = webdriver.ChromeOptions()

ops.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=ops)
driver.maximize_window()

try :
    wait = WebDriverWait(driver,10)
    
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(
        By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]'
    ).click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bike-light"
    ).click()
    ctn = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a/span').text

    assert ctn == "2"
    print("pass1")

    driver.find_element(By.XPATH,'//*[@id="remove-sauce-labs-onesie"]').click()

    assert driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a/span').text == "1"

    print("Pass2")


    
except Exception as e :
    filename = "failure.png"
    filepath = os.path.join(sc_path,filename)
    driver.save_screenshot(filepath)
    print("test case faild :",e)

