from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    __page_title_xpath = "//h5[contains(@class, 'orangehrm-login-title')]"
    __login_btn_xpath = "//button[contains(@class, 'orangehrm-login-button')]"
    __user_name_field_xpath = "//input[@name, 'username')]"
    __psw_field_xpath = "//input[@name, 'password')]"

    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self):
        title = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,  self.__page_title_xpath)))
        title_text = title.text
        assert title_text == "Login"

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.__login_btn_xpath).click()

    def fill_user_name(self, user_name="Admin"):
        self.driver.find_element(By.XPATH, self.__user_name_field_xpath).send_keys(user_name)
