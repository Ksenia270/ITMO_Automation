


from selenium import webdriver
from selenium.webdriver.common.by import By


def check_elements():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_element=driver.find_element(By.CSS_SELECTOR, "#user-name")
    password_element=driver.find_element(By.CSS_SELECTOR, "#password")
    submit_button=driver.find_element(By.CSS_SELECTOR, "#login-button")

    if username_element and password_element and submit_button:
        print("Элементы найдены")

    else:
        print("Произошла ошибка")

check_elements()