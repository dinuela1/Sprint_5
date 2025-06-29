from selenium.webdriver.support import expected_conditions as EC
import curl
from data_for_login import Credential
from locators import *


class TestLogin:
    def test_login_from_button(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button))
        driver.find_element(*HomePageLocators.login_account_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        assert driver.current_url == curl.main_page

    def test_login_from_account_link(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        assert driver.current_url == curl.main_page

    def test_login_from_registration_page(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.url_to_be(curl.login_page))
        driver.find_element(*LoginPageLocators.registration_link_button).click()
        wait.until(EC.url_to_be(curl.register_page))
        driver.find_element(*RegistrationPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.login_page))
        wait.until(EC.element_to_be_clickable(LoginPageLocators.email_input))
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        assert driver.current_url == curl.main_page

    def test_login_from_password_restoration_page(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.url_to_be(curl.login_page))
        driver.find_element(*LoginPageLocators.password_restoration_link_button).click()
        wait.until(EC.url_to_be(curl.forgot_password_page))
        driver.find_element(*ForgotPasswordLocators.login_button).click()
        wait.until(EC.url_to_be(curl.login_page))
        wait.until(EC.element_to_be_clickable(LoginPageLocators.email_input))
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        assert driver.current_url == curl.main_page

    def test_logout_from_account(self, driver, wait):
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button))
        driver.find_element(*HomePageLocators.login_account_button).click()
        driver.find_element(*LoginPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        driver.find_element(*LoginPageLocators.login_button).click()
        wait.until(EC.url_to_be(curl.main_page))
        driver.find_element(*HomePageLocators.account_link_button).click()
        wait.until(EC.element_to_be_clickable(AccountPageLocators.logout_button))
        driver.find_element(*AccountPageLocators.logout_button).click()
        wait.until(EC.url_to_be(curl.login_page))
        assert driver.current_url == curl.login_page
