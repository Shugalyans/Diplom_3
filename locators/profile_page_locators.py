from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #кнопка "Личный кабинет" на главной странице
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']") #кнопка история заказов в личном кабинете
    ORDERS_HISTORY_FIELD = (By.XPATH, "//*[@class='OrderHistory_listItem__2x95r mb-6']")  # Поле с историей заказов на странице История заказов в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка "Войти" на странице входа пользователя
    ENTER_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок Вход на странице авторизации