from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BrowsePage:
    url = ''
    loader_xpath = (By.XPATH, "//div[@class='oxd-circle-loader']")

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
        timeout = kwargs.get('timeout', 5)
        btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return btn.click()

    def fill_in_with_value(self, field, value, **kwargs):
        timeout = kwargs.get('timeout', 10)
        field_element = self.get_element(field, timeout=timeout)
        self.click_btn(field, timeout=timeout)
        field_element.send_keys(value)

    def delay_for_loading(self, **kwargs):
        timeout = kwargs.get('timeout', 20)
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(self.loader_xpath))
