from page_object.LoginPage import LoginPage
from utils import read_config


def test_1(setup):
    driver = setup
    driver.get(read_config.get_url())
    login_page = LoginPage(driver)

    login_page.verify_page_title()
