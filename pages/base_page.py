import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.start_page_locators import StartPageLocators
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем locator')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем что locator станет кликабельным')
    def wait_element_clickable(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Нажатие на locator')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скроллим к locator')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Вводим текст в locator')
    def enter_text(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_on_top_order_button(self):
        self.click_element(BasePageLocators.ON_TOP_ORDER_BUTTON)

    @allure.step('Кликаем на кнопку "Заказать" внизу страницы')
    def click_below_order_button(self):
        self.scroll_to_element(BasePageLocators.BELOW_ORDER_BUTTON)
        self.click_element(BasePageLocators.BELOW_ORDER_BUTTON)

    @allure.step('Переключаем активное окно браузера')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидаем URL текущей страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 6).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step('Закрытие окна с куками')
    def close_cookie_button(self):
        self.wait_element(BasePageLocators.BUTTON_COOKIE)
        self.click_element(BasePageLocators.BUTTON_COOKIE)

    @allure.step('Скроллим до визуального отображения вопросов')
    def scroll_question(self):
        self.scroll_to_element(StartPageLocators.INSCRIPTION_QUESTION_IMPORTANT)