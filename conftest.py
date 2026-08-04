import pytest
import requests
from faker import Faker
from selenium import webdriver

@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    yield drv
    drv.quit()

@pytest.fixture()
def registered_user():
    fake = Faker()
    username = fake.user_name()
    password = fake.password()
    response = requests.post('https://demoqa.com/Account/v1/User', json={'userName': username, 'password': password})
    return {'username': username, 'password': password}
