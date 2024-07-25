import allure
from data import MAIN_PAGE_URL, payload
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage

class TestLoginPage:
    @allure.title('Проверка переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_get_return_password_page_by_click_on_button(self, driver):
        login_page = LoginPage(driver)
        login_page.set_current_url(f'{MAIN_PAGE_URL}')
        login_page.wait_while_main_overlay_be_invisible()
        login_page.click(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.click(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)

        assert login_page.get_current_url() == f'{MAIN_PAGE_URL}forgot-password'

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_press_recovery_button(self, driver):
        login_page = LoginPage(driver)
        login_page.set_current_url(f'{MAIN_PAGE_URL}')
        login_page.wait_while_main_overlay_be_invisible()
        login_page.click(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.click(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        login_page.data_input_into_locator(LoginPageLocators.EMAIL_FIELD, payload['email'])
        login_page.click(LoginPageLocators.RECOVERY_BUTTON)
        login_page.wait_and_find_element(LoginPageLocators.ENTER_CODE)

        assert login_page.get_current_url() == f'{MAIN_PAGE_URL}reset-password'

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_check_password_field_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.set_current_url(f'{MAIN_PAGE_URL}')
        login_page.wait_while_main_overlay_be_invisible()
        login_page.click(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.data_input_into_locator(LoginPageLocators.PASSWORD_FIELD, payload['password'])
        login_page.click(LoginPageLocators.SHOW_PASS_BUTTON)

        visible_pass = login_page.wait_and_find_element(LoginPageLocators.VISIBLE_PASS)

        assert visible_pass.is_displayed