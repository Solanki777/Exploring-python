# Test case  

# webdriver is a module which is availbale in selenium package.

from selenium import webdriver


# 1. Open Web Browser(Chorme/firefox/Edge)

# to access drivers's clss we make a object for chrome
driver = webdriver.Chrome()
# Limit navigation wait to 20 seconds
driver.set_page_load_timeout(20)



# 2. Open Url https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")




# 3. Enter Username (Admin).

from selenium.webdriver.common.by import By

driver.find_element(By.NAME,"username").send_keys("Admin")


# 4.Enter Password(admin123).
driver.find_element(By.NAME,"password").send_keys("admin123")


# 5. Click on Login
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# # by text
# driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

# # by  class name 
# driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()



# 6. Capture title of the home page.(Actual Titile)
act_title = driver.title
exp_title = "OrangeHRM"



# 7. Verify title of the page : OrangeHRM (expected)

if exp_title == act_title :
    print("test pass")

else : print("test fail")


# 8. Close the brower
driver.close()