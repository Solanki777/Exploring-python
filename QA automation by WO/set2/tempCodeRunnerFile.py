
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sc_path = os.path.join(os.path.dirname(__file__), "..", "screenshots")
sc_path = os.path.abspath(sc_path)

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:

    driver.get("https://demoqa.com/automation-practice-form")

    # First Name
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.send_keys("Mahesh")

    # Last Name
    last_name = wait.until(
        EC.visibility_of_element_located((By.ID, "lastName"))
    )
    last_name.send_keys("Solanki")

    # Email
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "userEmail"))
    )
    email.send_keys("s@gmail.com")

    # Gender
    gender = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
        )
    )
    gender.click()

    # Mobile
    mobile = wait.until(
        EC.visibility_of_element_located((By.ID, "userNumber"))
    )
    mobile.send_keys("9725214521")

    # Submit
    submit = wait.until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit.click()

    # Verify successful submission
    result = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "example-modal-sizes-title-lg")
        )
    )

    assert result.text == "Thanks for submitting the form"

    print("PASS: Form submitted successfully")

except Exception as e:
    print("Test case failed:", e)

    filename = "practice_form_failure.png"
    filepath = os.path.join(sc_path, filename)
    driver.save_screenshot(filepath)

finally:
    driver.quit()
