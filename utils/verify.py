import time

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
        pass_msg = f'ASSERTION PASSED. Element with locator: {locator[1]} is present'
        fail_msg = f'Element with locator: {locator[1]} is NOT present'
    else:
        pass_msg = f'ASSERTION PASSED. Element {str(element_name)} is present'
        fail_msg = f'Element {str(element_name)} is NOT present'

    try:
        BrowsePage(driver).get_element(locator, timeout=timeout)
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.error(msg=f'{e.__class__.__name__}: {fail_msg}', error=TimeoutError)


def element_not_exists(driver, locator: tuple[str, str], **kwargs):
    delay = kwargs.get('delay', 2)
    timeout = kwargs.get('timeout', 5)
    element_name = kwargs.get('element_name', None)

    if element_name is None:
        pass_msg = f'ASSERTION PASSED. Element with locator: {locator[1]} is not present'
        fail_msg = f'Element with locator: {locator[1]} IS present'

    else:
        pass_msg = f'ASSERTION PASSED. {str(element_name)} is not present'
        fail_msg = f'{str(element_name)} IS present'

    try:
        time.sleep(delay)
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.error(msg=f'{e.__class__.__name__}: {fail_msg}', error=TimeoutError)


def verify_string(actual_str: str, expected_str: str, **kwargs):
    ignore_case = kwargs.get("ignore_case", False)
    if ignore_case:
        actual_str = actual_str.lower()
        expected_str = expected_str.lower()

    pass_msg = f'ASSERTION PASSED. Actual string: {str(actual_str)} is equal to expected: {str(expected_str)}'
    fail_msg = f'Actual string: {str(actual_str)} is NOT equal to expected: {str(expected_str)}'

    try:
        assert actual_str == expected_str
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.exception(msg=f'{e.__class__.__name__}: {fail_msg}')
        return False


def verify_element_text(driver, element_locator, expected_text: str, **kwargs):
    element = BrowsePage(driver).get_element(element_locator, **kwargs)
    element_text = element.text
    pass_msg = f'ASSERTION PASSED. Actual element text: {str(element_text)} is equal to expected: {str(expected_text)}'
    fail_msg = f'Actual element text: {str(element_text)} is NOT equal to expected: {str(expected_text)}'

    try:
        assert element_text == expected_text
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.exception(driver=driver, msg=f'{e.__class__.__name__}: {fail_msg}')
        return False
