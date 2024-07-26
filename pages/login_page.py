import allure
from data import payload
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step('Логинимся под пользователем')
    def login_user(self):
        self.wait_while_main_overlay_be_invisible()
        self.click(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        self.data_input_into_locator(LoginPageLocators.EMAIL_FIELD, payload['email'])
        self.data_input_into_locator(LoginPageLocators.PASSWORD_FIELD, payload['password'])
        self.click(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Прокидываем данные в локатор (если он поле ввода данных)')
    def data_input_into_locator(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

