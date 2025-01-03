import time

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