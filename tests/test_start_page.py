import pytest
import allure
from pages.start_page import StartPage
from data import answers_text


class TestStartPage:

    @allure.title('Проверка соответствия текста вопрос-ответ')
    @allure.description('Проверяем, что каждому вопросу соответствует нужный ответ')
    @pytest.mark.parametrize("index, text_answer",
                             [(0, answers_text[0]),
                              (1, answers_text[1]),
                              (2, answers_text[2]),
                              (3, answers_text[3]),
                              (4, answers_text[4]),
                              (5, answers_text[5]),
                              (6, answers_text[6]),
                              (7, answers_text[7])])
    def test_check_answer(self, driver, index, text_answer):
        start_page = StartPage(driver)
        start_page.close_cookie_button()
        start_page.scroll_question()
        question = start_page.click_question(index)
        result = start_page.search_answer(index)
        assert text_answer[question] == result
