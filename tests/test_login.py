from page_object.LoginPage import LoginPage
from utils.logger import Logger
from utils import verify

def test_1(driver):
    Logger.step("01", "test_1")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.verify_page_title()
    verify.element_exists(login_page.driver, login_page.page_title_xpath)
    verify.verify_string("d", "ewfwe")

def test_2(driver):
    Logger.step("2", "fdgre")
    assert 1 == 4
