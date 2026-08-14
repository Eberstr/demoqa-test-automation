import pytest
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless=new')
    drv = webdriver.Firefox(options=options)
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

    try:
        response = requests.post('https://demoqa.com/Account/v1/User', json={'userName': username, 'password': password})
    except requests.exceptions.RequestException as error:
        raise  Exception(f"Error al conectar a la API: {error}") from error

    if response.status_code == 201:
        return {'username': username, 'password': password}
    else:
        raise Exception (f'Error {response.text}')

@pytest.fixture
def faker():     
    return Faker()
