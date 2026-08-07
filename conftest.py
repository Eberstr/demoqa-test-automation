import pytest
import requests
from faker import Faker
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    yield drv
    drv.quit()

@pytest.fixture
def login_setup(driver):
    login = LoginPage(driver)
    login.setup()

    yield login

@pytest.fixture
def registered_user(faker):
    username = faker.user_name()
    password = faker.password()
    response = requests.post('https://demoqa.com/Account/v1/User', json={'userName': username, 'password': password})

    if response.status_code == 201:
        return {'username': username, 'password': password}

@pytest.fixture
def faker():     
    return Faker()
