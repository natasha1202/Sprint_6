import datetime as dt
import random

import pytest
from selenium import webdriver

import data
from page_object.page_locators.order_page_locators import OrderPageLocators
from page_object.pages.dzen_page import DzenPage
from page_object.pages.header_page import HeaderPage
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_url import PageUrl


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(PageUrl.MAIN_PAGE_URL)
    return MainPage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture(scope='function')
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture(scope='function')
def dzen_page(driver):
    return DzenPage(driver)


@pytest.fixture(scope='function')
def order_details():
    letters_low = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                   "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    letters_upper = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
                     "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ы", "Э", "Ю", "Я"]

    random_part_low = ''.join(random.choice(letters_low) for i in range(1, 10))
    random_part_upper = random.choice(letters_upper)
    random_phone = random.randint(1000000000, 9999999999)
    random_street_number = random.randint(100, 999)

    name = f'{random_part_upper}{random_part_low}'
    surname = f'{random_part_upper}{random_part_low}'
    phone = f'+7{random_phone}'
    address = f'Тестовая улица{random_street_number}'

    time_delta = random.randint(1, 10)
    future_date = dt.date.today() + dt.timedelta(days=time_delta)
    start_date = future_date.strftime("%d.%m.%Y")

    comment = random_part_low * 2

    return {"name": name,
            "surname": surname,
            "address": address,
            "phone": phone,
            "date": start_date,
            "comment": comment
            }
