from selenium.webdriver.common.by import By


class BasePageLocators:
    ON_TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav__AGCXC')]/button[text()='Заказать']")  # Кнопка
    # 'Заказать' вверху страницы

    BELOW_ORDER_BUTTON = (By.CSS_SELECTOR, "[class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка
    # 'Заказать' внизу страницы

    BUTTON_COOKIE = (By.ID, "rcc-confirm-button")  # Кнопка 'да все привыкли'
