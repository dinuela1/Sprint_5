from selenium.webdriver.common.by import By


class HomePageLocators:
    account_link_button = (By.XPATH, ".//p[text()='Личный Кабинет']")  # кнопка "Личный кабинет"
    login_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"


class LoginPageLocators:
    email_input = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле ввода эл.почты
    password_input = (By.XPATH, ".//input[@name='Пароль']")  # поле ввода пароля
    login_button = (By.XPATH, ".//button[text()='Войти']")  # кнопкa "войти"
    registration_link_button = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    password_restoration_link_button = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль"


class RegistrationPageLocators:
    name_input = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")   # поле ввода имени
    email_input = (By.XPATH, ".//label[text()='Email']/following-sibling::input")   # поле ввода эл.почты
    password_input = (By.XPATH, ".//input[@name='Пароль']")   # поле ввода пароля
    registration_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")   # кнопка "Зарегистрироваться"
    login_button = (By.XPATH, ".//a[text()='Войти']")   # кнопка "Войти


class ForgotPasswordLocators:
    login_button = (By.XPATH, ".//a[text()='Войти']")  # кнопка "Войти"


class AccountPageLocators:
    logout_button = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выйти"
    constructor = (By.XPATH, ".//p[text()='Конструктор']")  # Конструктор
    stellar_burgers = (By.XPATH, ".//a[@href='/']")


class Constructor:
    constructor = (By.XPATH, ".//p[text()='Конструктор']")  # Конструктор
    buns = (By.XPATH, ".//span[text()='Булки']")
    sauce = (By.XPATH, ".//span[text()='Соусы']")
    fillings = (By.XPATH, ".//span[text()='Начинки']")
