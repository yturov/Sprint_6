import allure
import pytest
from data import user_data
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка работоспособности функционала кнопки "Заказать" вверху страницы')
    @allure.description(
        'Проверка работоспособности функционала кнопки "Заказать" вверху страницы с двумя наборами данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*user_data])
    def test_successful_on_top_order_button(self, driver, name, surname, address, metro, number):
        order_page = OrderPage(driver)
        order_page.click_on_top_order_button()
        order_page.enter_data(name, surname, address, metro, number)
        text_order = order_page.successful_order()
        assert "Заказ оформлен" in text_order

    @allure.title('Проверка работоспособности функционала кнопки "Заказать" внизу страницы')
    @allure.description(
        'Проверка работоспособности функционала кнопки "Заказать" внизу страницы с двумя наборами данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*user_data])
    def test_successful_below_order_button(self, driver, name, surname, address, metro, number):
        order_page = OrderPage(driver)
        order_page.close_cookie_button()
        order_page.scroll_question()
        order_page.click_below_order_button()
        order_page.enter_data(name, surname, address, metro, number)
        text_order = order_page.successful_order()
        assert "Заказ оформлен" in text_order
