import allure
from locators.logo_page_locators import LogoPageLocators
from pages.base_page import BasePage


class LogoPage(BasePage):

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(LogoPageLocators.LOGO_YANDEX)

    @allure.step('Нажать логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(LogoPageLocators.LOGO_SCOOTER)

    @allure.step('Ожидаем что открытая страница в новом окне будет содержать url')
    def wait_for_url(self, url):
        self.switch_to_last_window()
        url = self.wait_url_contains(url)
        return url
