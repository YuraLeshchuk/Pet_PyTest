from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.general_methods.browse_page import BrowsePage
from utils import verify
from utils.logger import Logger
from utils import globals


class LoginPage(BrowsePage):
    url = "/auth/login"
    page_title_xpath = (By.XPATH, "//div[(@class='form-header')]")
    login_btn_xpath = (By.XPATH, "//button[(@type='submit')]")
    user_name_field_xpath = (By.XPATH, "//input[@id='txtUsername']")
    psw_field_xpath = (By.XPATH, "//input[@id='txtPassword']")
    login_error_form = (By.XPATH, "//div[contains(@class, 'toast-error')]")
    login = "Admin"
    psw = "aaaaaaaa"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load(self):
        self.get_page()

    def verify_page_title(self):
        verify.verify_element_text(self.driver, self.page_title_xpath, "Login")

    def click_login_btn(self):
        self.click_btn(self.login_btn_xpath)

    def fill_user_name(self, user_name: str):
        self.fill_in_with_value(self.user_name_field_xpath, user_name)

    def fill_psw(self, psw: str):
        self.fill_in_with_value(self.psw_field_xpath, psw)

    def login_with_user_credentials(self, user_name = login, psw = psw):
        self.fill_user_name(user_name)
        self.fill_psw(psw)
        self.click_login_btn()

    def verify_no_login_error(self):
        verify.element_not_exists(self.driver, self.login_error_form, element_name="Login Error Form", timeout=0)
