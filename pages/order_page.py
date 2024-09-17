import allure
from helpers import create_random_data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя')
    def input_name(self, name):
        self.enter_text(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Вводим фамилию')
    def input_surname(self, surname):
        self.enter_text(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.enter_text(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбор метро')
    def choice_metro(self, metro):
        self.click_element(OrderPageLocators.INPUT_METRO_STATION)
        self.enter_text(OrderPageLocators.INPUT_METRO_STATION, metro)
        self.click_element(OrderPageLocators.METRO_STATION)

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, number):
        self.enter_text(OrderPageLocators.INPUT_PHONE_NUMBER, number)

    @allure.step('Вводим дату начала аренды')
    def input_date_start_rent(self):
        date = create_random_data()
        self.enter_text(OrderPageLocators.INPUT_DATE, date)
        self.click_element(OrderPageLocators.TITLE_ABOUT_RENT)

    @allure.step('Выбор срока аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.FIVE_DAYS_RENT)

    @allure.step('Написание комментария')
    def comment_corier(self):
        self.enter_text(OrderPageLocators.INPUT_COMMENT_COURIER, "Тестим как можем хотим сдать спринт")

    @allure.step('Выставляем цвет самоката')
    def color_selection(self):
        self.click_element(OrderPageLocators.CHECKBOX_GREY)

    @allure.step('Вводим все пользовательские данные для заказа аренды')
    def enter_data(self, name, surname, address, metro, number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choice_metro(metro)
        self.input_phone_number(number)
        self.click_element(OrderPageLocators.BUTTON_NEXT)
        self.wait_element(OrderPageLocators.TITLE_ABOUT_RENT)
        self.input_date_start_rent()
        self.choose_rent_period()
        self.color_selection()
        self.comment_corier()
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.click_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Ожидаем окно подтверждения заказа')
    def successful_order(self):
        element = self.wait_element(OrderPageLocators.TITLE_SUCCESSFUL_ORDER)
        return element.text

