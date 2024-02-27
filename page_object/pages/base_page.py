from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def set_text_to_element(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    @staticmethod
    def calculate_locator(number, page_locator):
        method, locator = page_locator
        locator = locator.format(number)
        return method, locator

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))

