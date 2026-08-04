from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ProfilePage():
    URL = 'https://demoqa.com/profile'
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'button.btn-primary:nth-child(3)')
    
    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver.get(self.URL)
        return self

    def find_logout_button(self):
        self.logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        return self.logout_button

    def logout(self):
        self.find_logout_button().click()
