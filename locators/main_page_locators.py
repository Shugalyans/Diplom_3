from selenium.webdriver.common.by import By

class MainPageLocators:
   CREATE_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # Заголовок "Соберите бургер" на главной странице https://stellarburgers.nomoreparties.site/
   DETAILS_OF_INGREDIENT = (By.XPATH, "//*[@class = 'Modal_modal__container__Wo2l_']")  # всплывающее окно "Детали ингредиента" при нажатии на ингредиент
   INGREDIENT = (By.XPATH, "//*[contains(text(), 'Флюоресцентная')]")  # название ингредиента "Флюоресцентная Булка"
   INGREDIENT_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')][1]") #Крестик который находится в окне Детали ингредиента
   INGREDIENT_COUNTER = (By.XPATH, "//p[@class = 'counter_counter__num__3nue1']") #счетчик ингредиента
   BASKET = (By.XPATH, "//*[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']") # корзина куда закидываются ингредиенты
   ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной странице после входа в аккаунт
   YOUR_ORDER_PREPARING = (By.XPATH, "//*[contains(text(), 'Ваш заказ начали готовить')]") #инфо что заказ начали готовить
   ORDERS_LIST = (By.XPATH, "//h1[text()='Лента заказов']") #заголовок страницы лента заказов
