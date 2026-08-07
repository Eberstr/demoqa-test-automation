from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class RegisterPage():
    URL = 'https://demoqa.com/register'
    TIMEOUT = 10
    FIRSTNAME = (By.ID, 'firstname')
    LASTNAME = (By.ID, 'lastname')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    REGISTER_BUTTON = (By.ID, 'register')
    ERROR_PASSWORD_MESSAGE = (By.ID, 'name')

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver.get(self.URL)
    
        return self.driver

    def register(self, firstname: str, lastname: str, username: str, password: str):

        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.FIRSTNAME)).send_keys(firstname)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.LASTNAME)).send_keys(lastname)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.REGISTER_BUTTON)).click()

    def error_register_password_message(self):
        self.error_message = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.ERROR_PASSWORD_MESSAGE))
        return self.error_message.text