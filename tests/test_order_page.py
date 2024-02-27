import pytest
from page_object.page_locators.order_page_locators import OrderPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        "order_button",
        [
            MainPageLocators.ORDER_BUTTON_TOP,
            # MainPageLocators.ORDER_BUTTON_BOTTOM
        ]
    )
    def test_create_order_success(self, main_page, order_page, order_details, order_button):
        main_page.accept_cookie(MainPageLocators.ACCEPT_COOKIE_BUTTON)

        # Действия на главной странице
        if order_button == MainPageLocators.ORDER_BUTTON_BOTTOM:
            main_page.scroll_to_element(order_button)

        main_page.click_on_element(order_button)

        # Переход на страницу "Для кого самокат" и заполнение полей
        order_page.find_element_with_wait(OrderPageLocators.INPUT_NAME)
        order_page.set_text_to_element(OrderPageLocators.INPUT_NAME, order_details.get("name"))
        order_page.set_text_to_element(OrderPageLocators.INPUT_SURNAME, order_details.get("surname"))
        order_page.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, order_details.get("address"))
        order_page.click_on_element(OrderPageLocators.DROP_DOWN_METRO)
        order_page.select_item_from_drop_down(OrderPageLocators.STATION_OPTION_XPATH)
        order_page.set_text_to_element(OrderPageLocators.INPUT_PHONE, order_details.get("phone"))

        # Заполнение полей на странице "Про аренду"
        order_page.find_element_with_wait(OrderPageLocators.INPUT_DATE)
        order_page.set_text_to_element(OrderPageLocators.INPUT_DATE, order_details.get("date"))
        order_page.select_item_from_drop_down(
            OrderPageLocators.DROP_DOWN_RENT_PERIOD,
            order_details.get("period")
        )
        order_page.click_on_element(OrderPageLocators.CHECK_BOX_BLACK)
        order_page.set_text_to_element(OrderPageLocators.INPUT_COMMENT, order_details.get("comment"))

        # Подтверждение заказа
        order_page.click_on_element(OrderPageLocators.ORDER_BUTTON)

        order_page.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        order_page.click_on_element(OrderPageLocators.YES_BUTTON)

        # Проверка сообщения
        order_page.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_MESSAGE_HEADER)
        assert (order_page.get_text_from_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE_HEADER) ==
                'Заказ оформлен'), f'Заголовок сообщения неверный'

