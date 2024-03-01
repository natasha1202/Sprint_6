import allure

from page_object.page_locators.dzen_page_locators import DzenPageLocators
from page_object.page_locators.header_page_locators import HeaderPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators


class TestHeaderPage:

    @allure.description("Тест проверяет переход по логотипу Самокат")
    def test_click_on_scooter_logo(self, main_page, header_page):
        main_page.accept_cookie()
        header_page.click_on_logo()
        text_on_main_page = main_page.get_header_text_on_main_page()
        expected_text = 'Самокат\n'\
                        'на пару дней\n'\
                        'Привезём его прямо к вашей двери,\n'\
                        'а когда накатаетесь — заберём'
        assert main_page.check_text_on_page(text_on_main_page, expected_text)

    @allure.description("Тест проверяет переход по логотипу Яндекс")
    def test_redirect_to_dzen(self, main_page, header_page, dzen_page, driver):
        main_page.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADER_TEXT)
        header_page.switch_to_new_window(driver, HeaderPageLocators.YANDEX_LOGO_BUTTON)
        assert dzen_page.get_dzen_main_page_selected_tab(DzenPageLocators.DZEN_MAIN_PAGE_ELEMENT) == 'true'
