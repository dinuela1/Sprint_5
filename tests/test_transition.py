from selenium.webdriver.support import expected_conditions as EC
import curl
from data_for_login import Credential
from locators import *

class TestTransition:
    def test_transition_account_link_button(self, driver, wait):
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
        assert driver.current_url == curl.account_page

    def test_transition_from_account_to_construction(self, driver, wait):
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
        assert driver.current_url == curl.main_page

    def test_transition_from_account_to_stellar(self, driver, wait):
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
        driver.find_element(*AccountPageLocators.stellar_burgers).click()
        wait.until(EC.url_to_be(curl.main_page))
        assert driver.current_url == curl.main_page
