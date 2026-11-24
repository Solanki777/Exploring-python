from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")

    # Enter invalid username
    driver.find_element(By.ID, "user-name").send_keys("invalid")

    # Enter invalid password
    driver.find_element(By.ID, "password").send_keys("invalid")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    # Wait for error message
    wiat = WebDriverWait(driver,10)
    error_message = wiat.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    expected_message = (
        "Epic sadface: Username and password do not match "
        "any user in this service"
    )

    # Validate error message
    assert error_message.is_displayed()
    assert error_message.text == expected_message

    print("PASS: Invalid login rejected successfully")

    # Validate user remains on login page
    assert "inventory.html" not in driver.current_url

    print("PASS: User remains on login page")

except Exception as e:
    print("TEST FAILED:", e)
    raise

finally:
    driver.quit()
