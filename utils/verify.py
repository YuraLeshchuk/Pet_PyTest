from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger


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
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        Logger.checkpoint(pass_msg)
        return True
    except Exception as e:
        Logger.error(f'{e.__class__.__name__}: {fail_msg}', TimeoutError)


def verify_string(driver, expected_str: str, **kwargs):
    timeout = kwargs.get('timeout', 5)

    # pass_msg = f'T {str(element_name)} is present'
    # fail_msg = f'Element {str(element_name)} is NOT present'

    # try:
    #     element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    #     text = element.text
    #     assert text == expected_text
    #     Logger.checkpoint(pass_msg)
    #     return True
    # except Exception as e:
    #     Logger.error(f'{e.__class__.__name__}: {fail_msg}', TimeoutError)
