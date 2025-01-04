from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger
from page_object.general_methods.browse_page import BrowsePage


def element_exists(driver, locator: tuple[str, str], **kwargs):
    timeout = kwargs.get('timeout', 5)
    element_name = kwargs.get('element_name', None)
    if element_name is None:
        pass_msg = f'Element with locator: {locator[1]} is present'
        fail_msg = f'Element with locator: {locator[1]} is NOT present'
    else:
        pass_msg = f'Element {str(element_name)} is present'
        fail_msg = f'Element {str(element_name)} is NOT present'

    try:
        BrowsePage(driver).get_element(locator, timeout=timeout)
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.error(f'{e.__class__.__name__}: {fail_msg}', TimeoutError)


def verify_string(actual_str: str, expected_str: str, **kwargs):
    pass_msg = f'Actual string: {str(actual_str)} is equal to expected: {str(expected_str)}'
    fail_msg = f'Actual string: {str(actual_str)} is NOT equal to expected: {str(expected_str)}'

    try:
        assert actual_str == expected_str
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.exception(f'{e.__class__.__name__}: {fail_msg}')
        return False
