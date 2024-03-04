from selenium.webdriver.common.by import By


class MainPageLocators:

    # Вопрос из FAQ
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    # Тест ответа из FAQ
    ANSWER_LOCATOR = By.XPATH, ".//div[@id='accordion__panel-{}']/p"
    # Последний элемент на странице - блок с последним вопросом
    LAST_FAQ_ITEM = By.CSS_SELECTOR, ".accordion__item"

    # Кнопка Принять куки
    ACCEPT_COOKIE_BUTTON = By.ID, "rcc-confirm-button"

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = By.XPATH, ".//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]"
    ORDER_BUTTON_BOTTOM = By.XPATH, ".//div[contains(@class,'Home_FinishButton')]/button"

    # Текст заголовка страницы
    MAIN_PAGE_HEADER_TEXT = By.XPATH, ".//div[contains(@class,'Home_Header')]"

