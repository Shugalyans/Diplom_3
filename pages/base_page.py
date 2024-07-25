import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Очевидно дожидаемся нужного элемента по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажимаем на кнопку Конструктор вверху страницы')
    def constructor_button_click(self):
        self.click(BasePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на кнопку Лента Заказов вверху страницы')
    def orders_button_click(self):
        self.click(BasePageLocators.ORDERS_LOGO)

    @allure.step('Вводим нужный URL')
    def set_current_url(self, URL):
        self.driver.get(URL)

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидаем пока элемент исчезнет с страницы')
    def wait_while_main_overlay_be_invisible(self):
        WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(BasePageLocators.MAIN_LAYOUT))

    @allure.step('Ожидаем пока элемент станет доступен для нажатия')
    def wait_while_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        return True



