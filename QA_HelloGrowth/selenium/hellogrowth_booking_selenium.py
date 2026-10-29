
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Open Chrome browser
driver = webdriver.Chrome()
driver.set_page_load_timeout(20)

try:
    # 2. Open OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)

    # 3. Enter username
    wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    # 4. Enter password
    driver.find_element(By.NAME, "password").send_keys("admin123")

    # 5. Click Login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # 6. Wait until dashboard loads
    wait.until(EC.url_contains("/dashboard"))

    # 7. Capture and verify page title
    act_title = driver.title
    exp_title = "OrangeHRM"

    print("Actual title:", act_title)

    if act_title == exp_title:
        print("Test Pass")
    else:
        print("Test Fail")

finally:
    # 8. Close the complete browser session
    driver.quit()
