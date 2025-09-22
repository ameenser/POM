from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import utils.config as config
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)

    
def test_failed_login(driver):
    pass


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(), options=options)

    test_successful_login(driver)
    test_failed_login(driver)
