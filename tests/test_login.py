from page_object.LoginPage import LoginPage

def test_1(driver):
    driver.get(driver.base_url)
    login_page = LoginPage(driver)
    login_page.verify_page_title()

def test_2(driver):
    assert 1 == 4
