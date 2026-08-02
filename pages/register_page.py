from selenium import webdriver
from selenium.webdriver.common.by import By

class Register_page():
    def __init__(self):
        self.url = 'https://demoqa.com/register'
        self.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get(self.url)
        self.first_name_input = self.driver.find_element(by=By.ID, value='firstname')
        self.last_name_input = self.driver.find_element(by=By.ID, value='lastname')
        self.username_input = self.driver.find_element(by=By.ID, value='userName')
        self.password_input = self.driver.find_element(by=By.ID, value='password')
        self.register_button = self.driver.find_element(by=By.ID, value='register')
    
        return self.driver

    def register(self, firstname: str, lastname: str, username: str, password: str):
        self.first_name_input.send_keys(firstname)
        self.last_name_input.send_keys(lastname)
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.register_button.click()

    def teardown(self):
        self.driver.quit()