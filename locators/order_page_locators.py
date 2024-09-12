from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле ввода имени

    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле ввода фамилии

    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле ввода адреса

    INPUT_METRO_STATION = (By.CLASS_NAME, "select-search__input")  # Поле выпадающего списка  метро

    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле ввода телефона

    METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")  # Метро 'Сокольники'

    BUTTON_NEXT = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")  # Кнопка Далее

    TITLE_ABOUT_RENT = (By.CLASS_NAME, "Order_Header__BZXOb")  # Заголовок 'Про аренду' на странице заказа

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты для самоката

    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")  # Выпадающий список срока аренды

    FIVE_DAYS_RENT = (By.XPATH, "//div[@class = 'Dropdown-option' and text()='пятеро суток']")  # Вариант 'пятеро суток'

    CHECKBOX_GREY = (By.ID, "grey")  # Чекбокс выбор цвета самоката 'серая безысходность'

    INPUT_COMMENT_COURIER = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")  # Поле ввода комментария

    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")  #
    # Кнопка 'Заказать' для оформления заказа

    BUTTON_YES = (By.XPATH, "//button[text()='Да']")  # Кнопка 'Да'

    TITLE_SUCCESSFUL_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # Заголовок 'Заказ оформлен'

