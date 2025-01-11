from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.general_methods.browse_page import BrowsePage
from utils import verify
from utils.logger import Logger
from utils import globals


class LoginPage(BrowsePage):
    url = "/auth/login"
    page_title_xpath = (By.XPATH, "//h5[contains(@class, 'orangehrm-login-title')]")
    login_btn_xpath = (By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]")
    user_name_field_xpath = (By.XPATH, "//input[@name='username']")
    psw_field_xpath = (By.XPATH, "//input[@name='password']")
    login_form_xpath = (By.XPATH, "//div[@class='orangehrm-login-form']")
    error_form_xpath = (By.XPATH, "//div[contains(@class, 'oxd-alert--error')]")
    demo_credentials_container_xpath = (By.XPATH, "//div[contains(@class, 'orangehrm-demo-credentials')]//p")

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

    def get_default_credentials(self):
        demo_credentials = self.get_elements(self.demo_credentials_container_xpath)
        user_name = demo_credentials[0].text.split()[2]
        psw = demo_credentials[1].text.split()[2]
        return user_name, psw

    def login_with_default_credentials(self):
        user_name, psw = self.get_default_credentials()
        self.fill_user_name(user_name)
        self.fill_psw(psw)
        self.click_login_btn()

    def verify_no_login_error(self):
        verify.element_not_exists(self.driver, self.error_form_xpath, element_name="Login Error Form", timeout=0)
