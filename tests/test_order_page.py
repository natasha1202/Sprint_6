import allure
import pytest
from page_object.page_locators.order_page_locators import OrderPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators


class TestOrderPage:

    @pytest.mark.parametrize(
        "order_button",
        [
            MainPageLocators.ORDER_BUTTON_TOP,
            MainPageLocators.ORDER_BUTTON_BOTTOM
        ]
    )
    @allure.title("Тест - заказ самоката. Позитивный сценарий")
    @allure.description(
        "Параметризованный тест.\n"
        "Первый вариант заказ с помощью кнопки 'Заказать' вверху страницы\n"
        "Второй вариант заказ с помощью кнопки 'Заказать' внизу страницы\n"
        "Данные генерируются динамически"
    )
    def test_create_order_success(self, main_page, order_page, order_details, order_button):
        main_page.accept_cookie()
        main_page.click_on_order_button(order_button)

        order_page.fill_in_form_with_customer_details(order_details)
        order_page.click_on_next()
        order_page.fill_in_from_with_rent_details(order_details)

        order_page.submit_order()

        actual_message = order_page.get_text_of_message(OrderPageLocators.ORDER_SUCCESS_MESSAGE_HEADER)
        assert ('Заказ оформлен' and 'Номер заказа' and 'Запишите его') in actual_message, \
            f'Заголовок сообщения неверный'
