import pytest, time
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium import webdriver

def test_login_correct_credentials(driver, registered_user):
    login = LoginPage(driver)
    login.setup()
    login.login(registered_user['username'], registered_user['password'])
    profile = ProfilePage(driver)
    profile.setup()

    assert profile.find_logout_button()

@pytest.mark.skip()
def test_login_incorrect_credentials():
    pass

@pytest.mark.skip()
def test_login_incorrect_username():
    pass

@pytest.mark.skip()
def test_login_incorrect_password():
    pass