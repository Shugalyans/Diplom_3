from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")# Кнопка-эмблема "Конструктор" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    ORDERS_LOGO = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка-эмблема "Лента Заказов" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    MAIN_LAYOUT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading__3534A')]/following::div[@class='Modal_modal_overlay__x2ZCr']") #фон который перекрывает всю страницу и мешает прожать кнопки в Firefox
