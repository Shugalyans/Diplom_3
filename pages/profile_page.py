from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):

    @allure.step('Нажимаем на кнопку Личный кабинет вверху страницы')
    def profile_button_click(self):
        self.click(ProfilePageLocators.PROFILE_BUTTON)

    @allure.step('Нажимаем на кнопку История заказов в личном кабинете')
    def orders_history_button_click(self):
        self.click(ProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Нажимаем на Выход в личном кабинете')
    def logout_button_click(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Нажимаем на заказ из Истории заказов')
    def order_history_field_click(self):
        self.click(ProfilePageLocators.ORDERS_HISTORY_FIELD)
