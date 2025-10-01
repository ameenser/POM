from selenium.webdriver.common.by import By

def test_failed_wrong_cred_login(driver,pages):
    pages.login_page.login("wrong_user", "wrong_pass")
    error = pages.login_page.get_error_msg()
    assert "Username and password do not match any user in this service" in error


def test_failed_wrong_password_login(driver,pages):
    pages.login_page.login("standard_user", "wrong_pass")
    error = pages.login_page.get_error_msg()

    assert "Username and password do not match any user in this service" in error

def test_successful_login(driver, pages):
    pages.login_page.login("standard_user", "secret_sauce")  # use the page object
    header_label = pages.login_page.get_header_label()
    assert "Swag Labs" in header_label




