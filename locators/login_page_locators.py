from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  # поле "E-mail" для ввода
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  # поле "Пароль" для ввода
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти" на странице входа пользователя
    ENTER_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" на странице входа в аккаунт
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']") # кнопка "Восстановить" на странице восстановление пароля
    ENTER_CODE = (By.XPATH, "//label[text()='Введите код из письма']")  # поле для ввода кода из письма при восстановлении пароля
    SHOW_PASS_BUTTON = (By.XPATH, "//*[@class = 'input__icon input__icon-action']") #Кнопка-картинка "глаз" чтобы показать пароль
    VISIBLE_PASS = (By.XPATH, "//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']") # Активное поле с видимым паролем
