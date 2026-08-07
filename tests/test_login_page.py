import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium import webdriver

@pytest.mark.skip()
def test_login_correct_credentials(driver, registered_user, login_setup):
    login_setup.login(registered_user['username'], registered_user['password'])
    profile = ProfilePage(driver)
    profile.setup()

    assert profile.find_logout_button()

@pytest.mark.skip()
def test_login_incorrect_credentials(login_setup, faker):

    login_setup.login(faker.user_name(), faker.password())

    assert login_setup.error_login_message()

@pytest.mark.skip()
def test_login_incorrect_username(registered_user, login_setup, faker):

    login_setup.login(faker.user_name(), registered_user['password'])

    assert login_setup.error_login_message()

@pytest.mark.skip()
def test_login_incorrect_password(registered_user, login_setup, faker):

    login_setup.login(registered_user['username'], faker.password())

    assert login_setup.error_login_message()