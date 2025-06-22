from generator import generate_email
from selenium.webdriver.support import expected_conditions as EC
import curl
from data_for_registration import Credential, InValidPassword
from locators import HomePageLocators, LoginPageLocators, RegistrationPageLocators


def test_registration_valid_data(driver, wait):
    test_email = generate_email()
    wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
    driver.find_element(*HomePageLocators.account_link_button).click()
    wait.until(EC.element_to_be_clickable(LoginPageLocators.registration_link_button))
    driver.find_element(*LoginPageLocators.registration_link_button).click()
    driver.find_element(*RegistrationPageLocators.name_input).send_keys(Credential.name)
    driver.find_element(*RegistrationPageLocators.email_input).send_keys(test_email)
    driver.find_element(*RegistrationPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*RegistrationPageLocators.registration_button).click()
    wait.until(EC.url_to_be(curl.login_page))
    assert driver.current_url == curl.login_page


def test_registration_invalid_password(driver, wait):
    test_email = generate_email()
    wait.until(EC.element_to_be_clickable(HomePageLocators.account_link_button))
    driver.find_element(*HomePageLocators.account_link_button).click()
    wait.until(EC.element_to_be_clickable(LoginPageLocators.registration_link_button))
    driver.find_element(*LoginPageLocators.registration_link_button).click()
    driver.find_element(*RegistrationPageLocators.name_input).send_keys(InValidPassword.name)
    driver.find_element(*RegistrationPageLocators.email_input).send_keys(test_email)
    driver.find_element(*RegistrationPageLocators.password_input).send_keys(InValidPassword.password)
    driver.find_element(*RegistrationPageLocators.registration_button).click()
    wait.until(EC.url_to_be(curl.register_page))
    assert driver.current_url == curl.register_page
