
from selenium import webdriver

print("STEP 1: Starting Chrome...", flush=True)

driver = webdriver.Chrome()

print("STEP 2: Chrome launched!", flush=True)

driver.get("https://www.google.com/")

print("STEP 3: Website opened!", flush=True)

input("Press Enter to close browser...")

driver.quit()
