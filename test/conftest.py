import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_browser = Chrome(options=options)
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture
def main_page(browser):
    return MainPage(browser)
