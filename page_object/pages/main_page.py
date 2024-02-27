from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @staticmethod
    def check_answer(actual_text, expected_text):
        return actual_text == expected_text

    def accept_cookie(self, locator):
        self.click_on_element(locator)
