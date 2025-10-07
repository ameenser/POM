import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import utils.config as config
from pages.login_page import LoginPage
import tempfile


class Pages:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)


@pytest.fixture(scope="session")   # 👈 this makes it shared across ALL tests
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(), options=options)

    # Navigate once at the start
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service("/usr/local/bin/chromedriver")
    driver.get(config.BASE_URL)

    yield driver   # keep driver alive for all tests

    driver.quit()


@pytest.fixture(scope="session")
def pages(driver):
    return Pages(driver)