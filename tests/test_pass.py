from page_object.LoginPage import LoginPage
from utils.logger import Logger

def test_1(driver):
    Logger.step("01", "test_1")

    driver.get(driver.base_url)
    login_page = LoginPage(driver)
    login_page.verify_page_title()

def test_2(driver):
    Logger.step("2", "fdgre")
    assert 1 == 4
