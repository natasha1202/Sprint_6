from selenium.webdriver.common.by import By


class DzenPageLocators:

    # Значок логотипа Дзен
    DZEN_LOGO = By.XPATH, ".//a[(@aria-label='Логотип Бренда')]"
    # Кнопка для перехода на главную странцу Дзена. Подсвечивается при открытой главной странице
    DZEN_MAIN_PAGE_ELEMENT = By.XPATH, ".//span[contains(text(),'Главная')]"

    # Блок в котором находится кнопка "Главная"
    NAVIGATION_TAB_MAIN = By.XPATH, ".//span[contains(text(),'Главная')]/parent::div/parent::div/parent::li"
