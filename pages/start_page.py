import allure
from locators.start_page_locators import StartPageLocators
from pages.base_page import BasePage


class StartPage(BasePage):

    @allure.step('Нажимаем на вопрос')
    def click_question(self, index):
        selector, locator = StartPageLocators.QUESTION
        locator = locator.format(index)
        self.scroll_question()
        self.wait_element((selector, locator))
        self.click_element((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Поиск ответа на вопрос')
    def search_answer(self, index):
        selector, locator = StartPageLocators.ANSWER
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
