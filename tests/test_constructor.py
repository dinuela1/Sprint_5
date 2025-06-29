from selenium.webdriver.support import expected_conditions as EC
import curl
from data_for_login import Credential
from locators import *


class TestConstructor:
    def test_constructor_buns(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button))
        driver.find_element(*HomePageLocators.login_account_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.url_to_be(curl.account_page))
        driver.find_element(*AccountPageLocators.constructor).click()
        wait.until(EC.url_to_be(curl.main_page))
        buns_element = driver.find_element(*Constructor.buns)
        assert buns_element.is_displayed()

    def test_constructor_sauce(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button))
        driver.find_element(*HomePageLocators.login_account_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.url_to_be(curl.account_page))
        driver.find_element(*AccountPageLocators.constructor).click()
        wait.until(EC.url_to_be(curl.main_page))
        buns_element = wait.until(EC.visibility_of_element_located(Constructor.sauce))
        assert buns_element.is_displayed()

    def test_constructor_fillings(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button))
        driver.find_element(*HomePageLocators.login_account_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.url_to_be(curl.account_page))
        driver.find_element(*AccountPageLocators.constructor).click()
        wait.until(EC.url_to_be(curl.main_page))
        buns_element = wait.until(EC.visibility_of_element_located(Constructor.fillings))
        assert buns_element.is_displayed()
