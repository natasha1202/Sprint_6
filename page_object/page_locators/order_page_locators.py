from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Страница "Про аренду"
    INPUT_NAME = By.XPATH, ".//input[contains(@placeholder,'Имя')]"
    INPUT_SURNAME = By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"
    INPUT_ADDRESS = By.XPATH, ".//input[contains(@placeholder,'Адрес')]"
    INPUT_PHONE = By.XPATH, ".//input[contains(@placeholder,'Телефон')]"

    DROP_DOWN_METRO = By.XPATH, ".//input[contains(@placeholder,'Станция')]"
    STATION_LINE = By.CLASS_NAME, "select-search__input"
    STATION_OPTION_XPATH = By.XPATH, ".//li[(@class='select-search__row')and(@data-index=0)]"

    NEXT_BUTTON = By.XPATH, ".//button[contains(text(),'Далее')]"

    # Страница "Про аренду"

    INPUT_DATE = By.XPATH, ".//input[contains(@placeholder,'Когда')]"
    DROP_DOWN_RENT_PERIOD = By.XPATH, ".//div[contains(text(),'Срок аренды')]"
    CHECK_BOX_BLACK = By.ID, "black"
    CHECK_BOX_GREY = By.ID, "grey"
    INPUT_COMMENT = By.XPATH, ".//input[contains(@placeholder,'Комментарий')]"

    BACK_BUTTON = By.XPATH, ".//button[contains(text(),'Назад')]"
    ORDER_BUTTON = By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[contains(text(),'Заказать')]"

    # Форма "Хотите оформить заказ?"

    YES_BUTTON = By.XPATH, ".//button[contains(text(),'Да')]"
    NO_BUTTON = By.XPATH, ".//button[contains(text(),'Нет')]"

    ORDER_SUCCESS_MESSAGE_HEADER = ".//div[contains(@class,'Order_ModalHeader')]"
