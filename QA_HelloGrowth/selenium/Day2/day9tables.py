from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# static table 
# driver.get("https://testautomationpractice.blogspot.com/")

# driver.maximize_window()

# 1. count number of rows and columns 
# rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
# print("number of rows",rows)

# column = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//th"))

# print("number of column",column)


# 2. printing perticular data
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[3]").text 
# print(data)

# 3.print all data (make sure the here data is start from 1)
# i = 1
# for r in range(2,rows+1): # not using the first heading
#     print(i,".")
#     for c in range(1,column+1):
        
#         data = driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]")
#         print(data.text)
#     i += 1
#     print("\n")

# read based on the condition

# print("mukesh on top")
# i = 1
# for r in range(2,rows+1): 
#     if driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[2]").text == 'Mukesh':
#         print(i,".")
#         for c in range(1,column+1):
#                 data = driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]")
#                 print(data.text)
#         i+= 1
#         print("\n")
             
        
       
        
    


#  2 dynamic table  - Where the data is changing after some time but code will such that it will work on all the data for perticular condition that's all
