
import utils.config as config
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil
import pytest


class Pages:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)


@pytest.fixture(scope="session")   # 👈 this makes it shared across ALL tests
def driver():
    # ✅ create a unique temporary user-data-dir for each Jenkins run
    user_data_dir = tempfile.mkdtemp(prefix="chrome-profile-")

    options = Options()
    options.add_argument("--headless=new")              # run in headless mode for EC2
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # optional: to avoid “first run” popups
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")

    # Chrome driver (Selenium auto-detects path)
    driver = webdriver.Chrome(service=Service(), options=options)
    # Navigate once at the start
    driver.get(config.BASE_URL)

    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir, ignore_errors=True)


@pytest.fixture(scope="session")
def pages(driver):
    return Pages(driver)