import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from locators import *


class TestLoginAndRegistration:
    def test_registration_valid_data(self):
        account = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, ".//p[text()='Личный Кабинет']")))
        account.click()
        time.sleep(3)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, ".//label[text()='Имя']").click()
        driver.find_element(By.XPATH, ".//label[text()='Имя']").send_keys('Batman')

        time.sleep(3)
        driver.find_element(By.XPATH, ".//label[text()='Email']").send_keys("123@ya.ru")
        driver.find_element((By.XPATH, ".//label[text()='Пароль']"))


    def test_registration_invalid_password(self):



test_1 = TestLoginAndRegistration()
test_1.test_registration()
