import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger


@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    test_name = request.node.name
    logger, report_dir = Logger.setup_logger(test_name)
    driver._test_report_dir = report_dir

    logger.info(f"Starting test: {request.node.nodeid}")

    yield driver

    logger.info(f"Test {request.node.nodeid} finished")
    driver.quit()


def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        test_name = item.nodeid.split("::")[-1]
        report_dir = item.funcargs['driver']._test_report_dir
        Logger.save_screenshot(item.funcargs['driver'], report_dir, test_name)
        Logger.log_info(f"Test {item.nodeid} failed with {call.excinfo}")
