import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    yield drv
    drv.quit()