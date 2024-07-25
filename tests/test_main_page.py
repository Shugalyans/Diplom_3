import allure
from data import MAIN_PAGE_URL
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на лого Конструктор')
    @allure.description('Переходим на страницу списка заказов, после чего переходим на главную страницу, нажав на Конструктор')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.set_current_url(f'{MAIN_PAGE_URL}feed')
        main_page.wait_and_find_element(MainPageLocators.ORDERS_LIST)
        main_page.constructor_button_click()
        main_page.wait_and_find_element(MainPageLocators.CREATE_BURGER_HEADER)

        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.title('Проверка перехода по клику на кнопку "Список Заказов"')
    @allure.description('Переходим на главную страницу, после чего переходим на страницу заказов, нажав на "Список Заказов"')
    def test_orders_button(self, driver):
        main_page = MainPage(driver)
        main_page.set_current_url(MAIN_PAGE_URL)
        main_page.wait_while_main_overlay_be_invisible()
        main_page.orders_button_click()
        main_page.wait_and_find_element(MainPageLocators.ORDERS_LIST)

        assert main_page.get_current_url() == f'{MAIN_PAGE_URL}feed'

    @allure.title('Проверка перехода на детали ингредиента по клику на ингредиент')
    @allure.description('Переходим на всплывающее окно "Детали ингредиента", нажав на сам ингредиент')
    def test_get_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.set_current_url(MAIN_PAGE_URL)
        main_page.wait_and_find_element(MainPageLocators.INGREDIENT)
        main_page.ingredient_button_click()
        result = main_page.wait_and_find_element(MainPageLocators.DETAILS_OF_INGREDIENT)

        assert result.is_displayed


    @allure.title('Проверка закрытие информации об ингредиенте по нажатию крестика')
    @allure.description('Переходим на всплывающее окно "Детали ингредиента" нажав на ингредиент, нажимаем крестик, проверяем что закрылось')
    def test_close_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.set_current_url(MAIN_PAGE_URL)
        main_page.wait_and_find_element(MainPageLocators.INGREDIENT)
        main_page.ingredient_button_click()
        main_page.wait_and_find_element(MainPageLocators.DETAILS_OF_INGREDIENT)
        main_page.ingredient_close_button_click()

        assert main_page.wait_while_be_clickable(MainPageLocators.INGREDIENT) == True

    @allure.title('Проверка каунтера при нескольких перетягиваниях одинакового ингредиента')
    @allure.description('При добавлении ингредиента Флюоресцентная булка в заказ, увеличивается каунтер данного ингредиента до 2')
    def test_check_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.set_current_url(MAIN_PAGE_URL)
        main_page.ingredient_move_to_basket()

        assert main_page.ingredient_return_counter() == '2' # в Firefox тест падает так как не работает перетаскивание и счетчик не поднимается

    @allure.title('Проверка авторизованный пользователь может сделать заказ')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_authorized_user_create_order(self, driver, make_new_user):
        make_new_user
        main_page = MainPage(driver)
        main_page.set_current_url(MAIN_PAGE_URL)
        login_page = LoginPage(driver)
        login_page.login_user()
        main_page.ingredient_move_to_basket()
        main_page.create_order_button_click()
        result = main_page.wait_and_find_element(MainPageLocators.YOUR_ORDER_PREPARING)

        assert result.is_displayed