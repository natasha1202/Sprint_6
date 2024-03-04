import allure
import pytest

import data
from page_object.page_locators.main_page_locators import MainPageLocators


class TestMainPage:

    @pytest.mark.parametrize(
        "number, expected_text",
        [
            (0, data.ANSWER_1),
            (1, data.ANSWER_2),
            (2, data.ANSWER_3),
            (3, data.ANSWER_4),
            (4, data.ANSWER_5),
            (5, data.ANSWER_6),
            (6, data.ANSWER_7),
            (7, data.ANSWER_8)
        ]
    )
    @allure.title("FAQ проверка корректности пар вопрос-ответ")
    @allure.description("Тест проверяет текст ответов на вопросы")
    def test_question_answer_paar(self, main_page, number, expected_text):
        main_page.accept_cookie()
        actual_text = main_page.click_on_question_and_get_answer(number)

        assert main_page.check_answer(actual_text, expected_text), f'Actual answer do not match the question'
