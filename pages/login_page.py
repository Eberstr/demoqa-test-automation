from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    URL = 'https://demoqa.com/login'

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver.get(self.URL)

        return self.driver

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, value='userName').send_keys(username)
        self.driver.find_element(By.ID, value='password').send_keys(password)
        self.driver.find_element(By.ID, value='login').click()

    def error_login_message(self):
        return self.driver.find_element(By.ID, value='Invalid username or password!').text