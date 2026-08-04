from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class LoginPage():
    URL = 'https://demoqa.com/login'
    USER = (By.ID, 'userName')
    PASSWD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')
    LOGIN_ERROR = (By.LINK_TEXT, 'Invalid username or password!')
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver.get(self.URL)

        return self.driver

    def login(self, username: str, password: str):

        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.USER)).send_keys(username)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.PASSWD)).send_keys(password)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        time.sleep(5)

    def error_login_message(self):
        self.login_error_message = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.LOGIN_ERROR))
        return self.login_error_message.text