from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.general_methods.browse_page import BrowsePage
from utils import verify
from utils.logger import Logger
from utils import globals


class LoginPage(BrowsePage):
    url = "/auth/login"
    __page_title_xpath = (By.XPATH, "//h5[contains(@class, 'orangehrm-login-title')]")
    __login_btn_xpath = (By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]")
    __user_name_field_xpath = (By.XPATH, "//input[@name, 'username')]")
    __psw_field_xpath = (By.XPATH, "//input[@name, 'password')]")
    __login_form_xpath = (By.XPATH, "//div[@class='orangehrm-login-form']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_page_title(self):
        title = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.__page_title_xpath))
        title_text = title.text
        assert title_text == "Login"

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.__login_btn_xpath).click()

    def fill_user_name(self, user_name="Admin"):
        self.driver.find_element(By.XPATH, self.__user_name_field_xpath).send_keys(user_name)

    def load(self):
        self.get_page()
        verify.element_exists(self.driver, self.__login_form_xpath, element_name="Login Form")
        Logger.checkpoint("Login Page is opened")



