from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BrowsePage:
    url = ''

    def __init__(self, driver, **kwargs):
        self.driver = driver

    def get_page(self):
        self.driver.get(self.driver.base_url + self.url)

    def get_element(self, locator: tuple[str, str], **kwargs):
        timeout = kwargs.get('timeout', 5)
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def get_elements(self, locator: tuple[str, str], **kwargs):
        timeout = kwargs.get('timeout', 5)
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click_btn(self, locator: tuple[str, str], **kwargs):
        btn = self.get_element(locator, **kwargs)
        return btn.click()

    def fill_in_with_value(self, field, value):
        field = self.get_element(locator=field)
        field.click()
        field.send_keys(value)
