
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    print("Page title:", driver.title)

    # Open prompt alert
    driver.find_element(
        By.XPATH, '//*[@id="content"]/div/ul/li[3]/button'
    ).click()

    # Switch to alert
    alert = wait.until(EC.alert_is_present())

    # Enter text
    alert.send_keys("hello world")

    # Accept alert
    alert.accept()

    # Verify result
    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    )

    assert result.text == "You entered: hello world"

    print("PASS: Prompt alert handled successfully")

except Exception as e:
    print("TEST FAILED:", repr(e))
    raise

finally:
    driver.quit()
