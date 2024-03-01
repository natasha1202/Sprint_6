from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @staticmethod
    def check_answer(actual_text, expected_text):
        return actual_text == expected_text

    def accept_cookie(self):
        self.click_on_element(MainPageLocators.ACCEPT_COOKIE_BUTTON)

    def click_on_question_and_get_answer(self, number):
        question = self.calculate_locator(number, MainPageLocators.QUESTION_LOCATOR)
        answer = self.calculate_locator(number, MainPageLocators.ANSWER_LOCATOR)

        self.scroll_to_element(MainPageLocators.LAST_FAQ_ITEM)
        self.click_on_element(question)
        actual_text = self.get_text_from_element(answer)
        return actual_text

    def get_header_text_on_main_page(self):
        self.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADER_TEXT)

    @staticmethod
    def check_text_on_page(actual_text, expected_text):
        return actual_text == expected_text, f'Текст на соответствует ожидаемому'

    def click_on_order_button(self, order_button):
        if order_button == MainPageLocators.ORDER_BUTTON_BOTTOM:
            self.scroll_to_element(order_button)
        self.click_on_element(order_button)