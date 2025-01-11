import time

from page_object.LoginPage import LoginPage
from page_object.EmployeesPage import EmployeesPage
from page_object.EmployeesPage import AddEmployeeModal
from utils.logger import Logger


def test_1(driver):
    login_page = LoginPage(driver)
    employees_page = EmployeesPage(driver)
    add_employee_modal = AddEmployeeModal(driver)

    Logger.step("01", "Open Login Page")
    login_page.load()

    Logger.step("02", "Login with default user")
    login_page.login_with_user_credentials("Admin", "SX64ekR@Mn")
    login_page.verify_no_login_error()

    Logger.step("03", "Open Employee Page")
    employees_page.load()
    add_employee_modal.click_add_employee_btn()
    add_employee_modal.enter_first_name("efew")
    time.sleep(200)
