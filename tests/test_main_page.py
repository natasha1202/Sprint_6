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
    def test_question_answer_paar(self, main_page, number, expected_text):

        main_page.accept_cookie(MainPageLocators.ACCEPT_COOKIE_BUTTON)

        question = main_page.calculate_locator(number, MainPageLocators.QUESTION_LOCATOR)
        answer = main_page.calculate_locator(number, MainPageLocators.ANSWER_LOCATOR)

        main_page.scroll_to_element(MainPageLocators.LAST_FAQ_ITEM)
        main_page.click_on_element(question)
        actual_text = main_page.get_text_from_element(answer)
        assert main_page.check_answer(actual_text, expected_text), f'Actual answer do not match the question'
