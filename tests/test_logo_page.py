import allure
from data import URL_DZEN
from pages.logo_page import LogoPage
from pages.order_page import OrderPage


class TestLogoPage:

    @allure.title('Переход при нажатии на логотип "Яндекс"')
    @allure.description('Проверка перехода на главную страницу "Дзена" при нажатии на логотип "Яндекса"')
    def test_check_yandex_logo_click(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_yandex_logo()
        url = logo_page.wait_for_url(URL_DZEN)
        assert URL_DZEN in url

    @allure.title('Переход при нажатии на логотип "Самокат"')
    @allure.description('Проверка перехода на главную страницу «Самоката» со страницы заказа')
    def test_check_scooter_logo_click(self, driver):
        order_page = OrderPage(driver)
        logo_page = LogoPage(driver)
        order_page.click_on_top_order_button()
        order_url = driver.current_url
        logo_page.click_scooter_logo()
        scooter_url = driver.current_url
        assert order_url != scooter_url
