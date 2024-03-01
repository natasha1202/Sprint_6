from page_object.page_locators.header_page_locators import HeaderPageLocators
from page_object.pages.base_page import BasePage


class HeaderPage(BasePage):

    def switch_to_new_window(self, driver, locator):
        header_page = HeaderPage(driver)
        window_before = driver.window_handles[0]
        header_page.click_on_element(locator)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

    def click_on_logo(self):
        self.click_on_element(HeaderPageLocators.YANDEX_LOGO_BUTTON)
