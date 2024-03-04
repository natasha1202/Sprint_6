import allure

from page_object.page_locators.dzen_page_locators import DzenPageLocators
from page_object.pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step("Выбрать таб с название главной страницы")
    def get_dzen_main_page_selected_tab(self, locator):
        self.find_element_with_wait(locator)
        element = self.driver.find_element(*DzenPageLocators.NAVIGATION_TAB_MAIN)
        return element.get_attribute("aria-selected")
