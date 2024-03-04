import random

import allure

from page_object.page_locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнение полей на странице 'Для кого самокат'")
    def fill_in_form_with_customer_details(self, order_details):
        self.find_element_with_wait(OrderPageLocators.INPUT_NAME)
        self.set_text_to_element(OrderPageLocators.INPUT_NAME, order_details.get("name"))
        self.set_text_to_element(OrderPageLocators.INPUT_SURNAME, order_details.get("surname"))
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, order_details.get("address"))
        self.select_element_from_drop_down(OrderPageLocators.DROP_DOWN_METRO, OrderPageLocators.STATION_ITEM)
        self.wait_for_element(OrderPageLocators.INPUT_PHONE)
        self.set_text_to_element(OrderPageLocators.INPUT_PHONE, order_details.get("phone"))

    @allure.step("Нажать кнопку 'Далее'")
    def click_on_next(self):
        self.wait_for_element(OrderPageLocators.NEXT_BUTTON)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение полей на странице 'Про аренду'")
    def fill_in_from_with_rent_details(self, order_details):
        self.find_element_with_wait(OrderPageLocators.INPUT_DATE)
        self.set_text_to_element(OrderPageLocators.INPUT_DATE, order_details.get("date"))
        self.click_on_element(self.choose_color())
        self.set_text_to_element(OrderPageLocators.INPUT_COMMENT, order_details.get("comment"))
        self.select_element_from_drop_down(OrderPageLocators.DROP_DOWN_RENT_PERIOD, OrderPageLocators.PERIOD_OPTION)
        self.wait_for_element(OrderPageLocators.INPUT_COMMENT)

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Выявить текст сообщения")
    def get_text_of_message(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Выбрать цвет")
    def choose_color(self):
        colors = [OrderPageLocators.CHECK_BOX_BLACK,
                  OrderPageLocators.CHECK_BOX_GREY]
        return random.choice(colors)
