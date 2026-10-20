from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.get("https://demo.automationtesting.in/Index.html")
email_txt = driver.find_element(By.ID,'email')
email_txt.send_keys("test@gamil.com")
driver.find_element(By.ID,"enterimg").click()