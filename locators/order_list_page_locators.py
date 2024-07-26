from selenium.webdriver.common.by import By

class OrderListPageLocators:
    CLOSE_ORDER_INFO = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Крестик закрыть окно с деталями заказа после оформления заявки
    ORDER_DETAILS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']") # Окно с деталями заказа, которое открывается в Истории заказов после нажатия на соответствующий заказ
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']") # Окно с деталями заказа и его номером после оформления заказа
    TOTAL_ORDERS = (By.XPATH, "//*[contains(text(), 'за все время')]/following::p") #счетчик заказов за все время
    TOTAL_ORDERS_TODAY = (By.XPATH, "//*[contains(text(), 'сегодня')]/following::p") #счетчик заказов за сегодня
    ORDER_ID = (By.XPATH, "//*[contains(@class, 'Modal_modal__contentBox')]/child::h2") #ID заказа после его создания
    ORDER_IN_WORK_BASE = (By.XPATH, "//*[contains(@class, 'orderListReady')]/child::li[@class='text text_type_main-small']")  # номер заказа в статусе В работе
    ORDER_IN_WORK_NEW = (By.XPATH, "//*[contains(@class, 'orderListReady')]/child::li[@class='text text_type_digits-default mb-2']")  # номер заказа в статусе В работе
