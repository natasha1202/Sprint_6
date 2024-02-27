from page_object.page_locators.dzen_page_locators import DzenPageLocators
from page_object.page_locators.header_page_locators import HeaderPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators


class TestHeaderPage:

    def test_click_on_scooter_logo(self, main_page, header_page):
        main_page.accept_cookie(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        header_page.click_on_element(HeaderPageLocators.YANDEX_LOGO_BUTTON)
        text_on_main_page = main_page.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADER_TEXT)
        assert text_on_main_page.text == ('Самокат\n'
                                          'на пару дней\n'
                                          'Привезём его прямо к вашей двери,\n'
                                          'а когда накатаетесь — заберём')

    def test_redirect_to_dzen(self, main_page, header_page, dzen_page, driver):
        main_page.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADER_TEXT)
        header_page.switch_to_new_window(driver, HeaderPageLocators.YANDEX_LOGO_BUTTON)
        dzen_page.driver = driver
        assert dzen_page.get_dzen_main_page_selected_tab(DzenPageLocators.DZEN_MAIN_PAGE_ELEMENT) == 'true'

