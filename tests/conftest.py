import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import curl


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(curl.main_page)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 5)
