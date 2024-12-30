import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.logger import Logger


@pytest.fixture()
def get_test_name(request):
    return request.node.name


@pytest.fixture()
def setup(get_test_name):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    Logger.setup_loger(get_test_name)
    Logger.scenario_start(get_test_name)



    yield driver
    Logger.scenario_summary()
    driver.quit()

