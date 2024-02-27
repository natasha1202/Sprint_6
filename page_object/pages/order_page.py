from page_object.page_locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):
    def select_element_from_drop_down(self, locator, index):
        select = Select(self.driver.find_element_by_xpath(locator))
        # select.select_by_visible_text(text)
        select.select_by_index(index)

    def select_item_from_drop_down(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        Select(element).first_selected_option.click()

    def set_station(self, text='Преображенская площадь'):
        # select = Select(self.find_element_with_wait(OrderPageLocators.DROP_DOWN_METRO))
        element = self.driver.find_element(*OrderPageLocators.DROP_DOWN_METRO)
        element.click()
        select.select_by_visible_text(text)

    def set_rent_period(self, text='Сутки'):
        # select = Select(self.find_element_with_wait(OrderPageLocators.DROP_DOWN_METRO))
        element = self.driver.find_element_by_xpath(OrderPageLocators.DROP_DOWN_RENT_PERIOD)
        element.click()
        select.select_by_visible_text(text)


