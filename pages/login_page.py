from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_page():
    def __init__(self):
        self.url = 'https://demoqa.com/login'
        self.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get(self.url)
        self.username_input = self.driver.find_element(by=By.ID, value='userName')
        self.password_input = self.driver.find_element(by=By.ID, value='password')
        self.login_button = self.driver.find_element(by=By.ID, value='login')

        return self.driver

    def login(self, username: str, password: str):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def teardown(self):
        self.driver.quit()
