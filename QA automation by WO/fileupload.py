import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/automation-practice-form")

    # Absolute path of your image
    file_path = os.path.abspath("testchrome.py")

    # Verify file exists before uploading
    assert os.path.isfile(file_path), "File does not exist!"

    # Upload file
    upload = driver.find_element(By.ID, "uploadPicture")
    upload.send_keys(file_path)

    # Validate uploaded filename
    uploaded_file = driver.find_element(By.ID, "uploadPicture").get_attribute("value")

    assert os.path.basename(file_path) in uploaded_file

    print("PASS: File uploaded successfully")

finally:
    driver.quit()