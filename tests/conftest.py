import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import curl


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome
    driver.get(curl.main_page)
    driver.maximize_window()
    yield driver
    driver.quit()


