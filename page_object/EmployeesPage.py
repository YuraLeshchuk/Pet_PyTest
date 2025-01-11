from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.general_methods.browse_page import BrowsePage
from utils import verify
from utils.logger import Logger
from utils import globals


class EmployeesPage(BrowsePage):
    url = "/client/#/pim/employees"

    page_title_xpath = (By.XPATH, "//li[contains(@class, 'page-title')]//div")
    add_employee_btn_xpath = (By.XPATH, "//a[@id='addEmployeeButton']")
    loader_xpath = (By.XPATH, "//div[@class='oxd-circle-loader']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load(self):
        self.get_page()

    def verify_page_title(self):
        verify.verify_element_text(self.driver, self.page_title_xpath, "Employee Management")

    def click_add_employee_btn(self):
        self.click_btn(self.add_employee_btn_xpath, timeout=10)
        self.delay_for_loading()


class AddEmployeeModal(EmployeesPage):
    first_name_field_xpath = (By.XPATH, "//input[@id='first-name-box']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_first_name(self, first_name: str):
        self.fill_in_with_value(self.first_name_field_xpath, first_name)
