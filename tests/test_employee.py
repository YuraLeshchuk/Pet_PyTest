import time

from page_object.LoginPage import LoginPage
from page_object.general_methods.browse_page import BrowsePage
from page_object.EmployeesPage import EmployeesPage
from page_object.EmployeesPage import AddEmployeeModal
from utils.logger import Logger


def test_1(driver):
    browse = BrowsePage(driver)
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
    add_employee_modal.load_photo(r"\test_data\duck.jpg")
    browse.set_mouse_cursor(625, 390)
    browse.click_and_move_mouse_cursor(0, -40)
    file = r'C:\Users\yura7\Desktop\Pet_PyTest\test_data\users.xlsx'
    add_employee_modal.create_user_from_xl(file, "users", 1)
