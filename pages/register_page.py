from selenium import webdriver
from selenium.webdriver.common.by import By

class RegisterPage():
    URL = 'https://demoqa.com/register'


    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver.get(self.URL)
    
        return self.driver

    def register(self, firstname: str, lastname: str, username: str, password: str):
        self.driver.find_element(by=By.ID, value='firstname').send_keys(firstname)
        self.driver.find_element(by=By.ID, value='lastname').send_keys(lastname)
        self.driver.find_element(by=By.ID, value='userName').send_keys(username)
        self.driver.find_element(by=By.ID, value='password').send_keys(password)
        self.driver.find_element(by=By.ID, value='register').click()

    def error_register_password_message(self):
        return self.driver.find_element(By.ID, value='name').text