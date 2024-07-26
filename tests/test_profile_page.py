import allure
from data import MAIN_PAGE_URL, LOGIN_PAGE_URL, ORDER_HISTORY_PAGE_URL
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

class TestProfilePage:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_click_on_profile_button(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.set_current_url(MAIN_PAGE_URL)
        profile_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.profile_button_click()

        assert profile_page.get_current_url() == LOGIN_PAGE_URL


    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('переход в раздел «История заказов»')
    def test_click_on_orders_history_button(self, driver, make_new_user):
        login_page = LoginPage(driver)
        login_page.login_user()
        profile_page = ProfilePage(driver)
        profile_page.wait_while_main_overlay_be_invisible() # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.profile_button_click()
        profile_page.wait_and_find_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        profile_page.wait_while_main_overlay_be_invisible() # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.orders_history_button_click()

        assert profile_page.get_current_url() == ORDER_HISTORY_PAGE_URL

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка, что можно выйти из аккаунта, нажав соответствующую кнопку')
    def test_click_on_logout_button(self, driver, make_new_user):
        login_page = LoginPage(driver)
        login_page.login_user()
        profile_page = ProfilePage(driver)
        profile_page.wait_while_main_overlay_be_invisible() # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.profile_button_click()
        profile_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.logout_button_click()
        profile_page.wait_and_find_element(ProfilePageLocators.ENTER_HEADER)

        assert profile_page.get_current_url() == LOGIN_PAGE_URL