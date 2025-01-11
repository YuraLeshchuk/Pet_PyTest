from page_object.LoginPage import LoginPage
from utils.logger import Logger


def test_1(driver):
    login_page = LoginPage(driver)

    Logger.step("01", "Open Login Page")
    login_page.load()

    Logger.step("02", "Verify Login Page loaded")
    login_page.verify_page_title()

    Logger.step("03", "Login with default user")
    login_page.login_with_user_credentials("Admin", "SX64ekR@Mn")
    login_page.verify_no_login_error()



def test_2(driver):
    Logger.step("2", "fdgre")
    assert 1 == 3
