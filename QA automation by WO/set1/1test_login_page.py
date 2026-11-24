from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"
    print("Pass1")

    username = driver.find_element(By.ID, "user-name")
    assert username.is_displayed()
    print("pass2")

    password = driver.find_element(By.ID,"password")
    assert password.is_displayed()
    print("pass3")

    login = driver.find_element(By.ID, "login-button")
    assert login.is_displayed()
    assert login.is_enabled()
    print("Pass4")

    print("all test casees passed")



except Exception as e:print(e)