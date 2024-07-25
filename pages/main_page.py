import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Нажимаем на индгредиент Флюоресцентная булка')
    def ingredient_button_click(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step('Нажимаем на кнопку Крестик в окне Детали ингредиента')
    def ingredient_close_button_click(self):
        self.click(MainPageLocators.INGREDIENT_CLOSE_BUTTON)

    @allure.step('Перетягиваем элемент в корзину')
    def ingredient_move_to_basket(self):
        drag = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(MainPageLocators.INGREDIENT))
        drop = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(MainPageLocators.BASKET))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Возвращаем значение счетчика ингредиента')
    def ingredient_return_counter(self):
        result = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER)).text
        return result

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def create_order_button_click(self):
        self.click(MainPageLocators.ORDER_BUTTON)

