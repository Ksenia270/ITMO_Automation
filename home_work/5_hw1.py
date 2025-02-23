from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
text=driver.find_element(By.CSS_SELECTOR, '#user-name')
if text is None:
    print ('Элемент не найден')
else:
    print('Элемент найден')




from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
text = driver.find_element(By.CSS_SELECTOR, '#password')
if text is None:
    print('Элемент не найден')
else:
     print('Элемент найден')



from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

button=driver.find_element(By.CSS_SELECTOR, '#login-button')
if button is None:
    print ('Элемент не найден')
else:
    print('Элемент найден')