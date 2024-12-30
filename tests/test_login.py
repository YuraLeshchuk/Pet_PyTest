from page_object.LoginPage import LoginPage
from utils import read_config


def test_1(driver):
    driver.get(read_config.get_url())
    login_page = LoginPage(driver)

    login_page.verify_page_title()

def test_2(driver):
    assert 1 == 4
