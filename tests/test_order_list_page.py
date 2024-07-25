import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from data import MAIN_PAGE_URL
from pages.profile_page import ProfilePage
from locators.order_list_page_locators import OrderListPageLocators



class TestOrderListPage:

    @allure.title('Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_and_see_details(self, driver, make_new_user):
        make_new_user
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)

        order_list_page.set_current_url(MAIN_PAGE_URL) #заходим на главную страницу
        login_page.login_user() # создадим пользователя и залогинимся под ним
        main_page.ingredient_move_to_basket() # закинем ингредиенты в корзину
        main_page.create_order_button_click() # появилась кнопка Оформить заказ, кликаем на нее
        order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER) # появилось окно с номером заказа и его информацией
        order_list_page.wait_while_main_overlay_be_invisible()# убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        order_list_page.order_details_close_button_click() # кликаем на крестик чтобы закрыть окно с номером заказа
        order_list_page.wait_while_main_overlay_be_invisible()# убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.profile_button_click() # кликаем на кнопку Личный кабинет
        order_list_page.wait_while_main_overlay_be_invisible() # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.wait_and_find_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        profile_page.orders_history_button_click() # ожидаем, что попали в личный кабинет пользователя, нажимаем на кнопку История заказов
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.wait_and_find_element(ProfilePageLocators.ORDERS_HISTORY_FIELD)
        profile_page.order_history_field_click()# ожидаем появление окна с заказами, нажимаем на него
        result = order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_DETAILS) #ожидаем появления окна с деталями заказа из Истории заказов, сохраняем в переменную чтобы проверить assert

        assert result.is_displayed

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_are_visible_in_profile(self, driver, make_new_user):
        make_new_user
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)

        order_list_page.set_current_url(MAIN_PAGE_URL) #заходим на главную страницу
        login_page.login_user() # создадим пользователя и залогинимся под ним
        main_page.ingredient_move_to_basket() # закинем ингредиенты в корзину
        main_page.create_order_button_click() # появилась кнопка Оформить заказ, кликаем на нее
        order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER) # появилось окно с номером заказа и его информацией
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        order_list_page.order_details_close_button_click() # кликаем на крестик чтобы закрыть окно с номером заказа
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.profile_button_click() # кликаем на кнопку Личный кабинет
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        profile_page.orders_history_button_click() # ожидаем, что попали в личный кабинет пользователя, нажимаем на кнопку История заказов
        result = profile_page.wait_and_find_element(ProfilePageLocators.ORDERS_HISTORY_FIELD) # ожидаем появление окна с заказами

        assert result.is_displayed # в Firefox не отображаются заказы в Истории заказов, тест падает

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_total_orders_counter(self, driver, make_new_user):
        make_new_user
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        main_page = MainPage(driver)

        total_counter_base = order_list_page.get_total_orders_counter(OrderListPageLocators.TOTAL_ORDERS)# вызываем метод который выводит текущий счетчик заказов. Он будет базой для сравнения
        print('Было заказов за все время:  ', total_counter_base)
        # создадим новый заказ, чтобы проверить увеличение счетчика
        order_list_page.set_current_url(MAIN_PAGE_URL) #заходим на главную страницу
        login_page.login_user() # создадим пользователя и залогинимся под ним
        main_page.ingredient_move_to_basket() # закинем ингредиенты в корзину
        main_page.create_order_button_click() # появилась кнопка Оформить заказ, кликаем на нее
        order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER) # появилось окно с номером заказа и его информацией
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        order_list_page.order_details_close_button_click() # кликаем на крестик чтобы закрыть окно с номером заказа
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        total_counter_new = order_list_page.get_total_orders_counter(OrderListPageLocators.TOTAL_ORDERS)# вызываем метод который выводит текущий счетчик заказов. Его значение должно быть больше исходного, так как мы создали новый заказ
        print('Стало заказов за все время:  ', total_counter_new)

        assert total_counter_base < total_counter_new # в Firefox счетчик не работает и получается что заказы равны и тест падает

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_total_orders_today_counter(self, driver, make_new_user):
        make_new_user
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        main_page = MainPage(driver)

        total_counter_base = order_list_page.get_total_orders_counter(OrderListPageLocators.TOTAL_ORDERS_TODAY)# вызываем метод который выводит текущий счетчик заказов. Он будет базой для сравнения
        print('Было заказов за сегодня:  ', total_counter_base)
        # создадим новый заказ, чтобы проверить увеличение счетчика
        order_list_page.set_current_url(MAIN_PAGE_URL) #заходим на главную страницу
        login_page.login_user() # создадим пользователя и залогинимся под ним
        main_page.ingredient_move_to_basket() # закинем ингредиенты в корзину
        main_page.create_order_button_click() # появилась кнопка Оформить заказ, кликаем на нее
        order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER) # появилось окно с номером заказа и его информацией
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        order_list_page.order_details_close_button_click() # кликаем на крестик чтобы закрыть окно с номером заказа
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        total_counter_new = order_list_page.get_total_orders_counter(OrderListPageLocators.TOTAL_ORDERS_TODAY)# вызываем метод который выводит текущий счетчик заказов. Его значение должно быть больше исходного, так как мы создали новый заказ
        print('Стало заказов за сегодня:  ', total_counter_new)

        assert total_counter_base < total_counter_new # в Firefox счетчик не работает и получается что заказы равны и тест падает


    @allure.title('Проверка, что при оформлении нового заказа его номер появляется в Ленте заказов в статусе в Работе')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_number(self, driver, make_new_user):
        make_new_user
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        main_page = MainPage(driver)

        # создадим новый заказ, чтобы получить его номер
        order_list_page.set_current_url(MAIN_PAGE_URL) # заходим на главную страницу
        login_page.login_user() # создадим пользователя и залогинимся под ним
        main_page.ingredient_move_to_basket() # закинем ингредиенты в корзину
        main_page.create_order_button_click() # появилась кнопка Оформить заказ, кликаем на нее
        order_list_page.wait_while_be_clickable(OrderListPageLocators.CLOSE_ORDER_INFO) # Ждем пока окно с информацией о заказе прогрузится
        order_list_page.wait_while_text_change() # Ждем пока в окне с информацией о заказе изменится базовый ID=9999
        order_id = order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_ID).text # появилось окно с информацией по заказу, берем оттуда номер заказа
        print('Номер заказа: ', order_id) # появилось окно с номером заказа и его информацией
        order_list_page.order_details_close_button_click() # кликаем на крестик чтобы закрыть окно с номером заказа
        # зайдем в Ленту заказов и проверим что наш заказ находится в статусе В работе
        order_list_page.orders_button_click() # кликаем на кнопку Лента заказов
        order_list_page.wait_while_main_overlay_be_invisible()  # убираем фон, который перекрывает страницу в Firefox и мешает нажать на локатор
        order_in_work = order_list_page.wait_and_find_element(OrderListPageLocators.ORDER_IN_WORK_NEW).text # ищем локатор с номером заказа в поле В работе

        print('Номер заказа в работе: ', order_in_work)

        assert f'0{order_id}' == order_in_work # в Firefox тест зависает на окне с номером заказа