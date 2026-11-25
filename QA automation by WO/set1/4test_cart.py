from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ops = webdriver.ChromeOptions()

ops.add_argument("--disable-features=PasswordManagerOnboarding")

driver = webdriver.Chrome(options=ops)
driver.maximize_window()

try :
    wait = WebDriverWait(driver,10)
    
    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    
    username.send_keys("standard_user")

    passwd = wait.until(EC.visibility_of_element_located((By.ID,"password")))
    passwd.send_keys("secret_sauce")
    
    driver.find_element(By.ID, "login-button").click()

    bg_button = wait.until(EC.visibility_of_element_located((
        By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]'
    )))
    bg_button.click()

    biekbutn = wait.until(EC.visibility_of_element_located((
        By.ID, "add-to-cart-sauce-labs-bike-light"
    )))

    biekbutn.click()

    ctn = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="shopping_cart_container"]/a/span'))).text

    assert ctn == "2"
    print("pass1")

    onesie = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="remove-sauce-labs-onesie"]')))
    onesie.click()


    assert driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a/span').text == "1"

    print("Pass2")

    driver.find_element(By.ID,'remove-sauce-labs-bike-light').click()
    print("Pass3")

    assert len(driver.find_elements(
    By.XPATH, '//*[@id="shopping_cart_container"]/a/span'
)) == 0
  
    print("Pass4")



    
except Exception as e :
    print("test case faild :",e)

finally: driver.quit()