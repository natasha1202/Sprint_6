from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # Логотип "Самокат"
    LOGO_BUTTON = By.XPATH, ".//a[(@href='/')]"
    # Логотип "Яндекс"
    YANDEX_LOGO_BUTTON = By.XPATH, ".//a[(@href= '//yandex.ru')]"
