import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger, initialize_logger
from utils import globals
from utils import read_config

# Створення загальної папки для запуску тестів
RUN_TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
TEST_RUN_DIR = os.path.join("reports", f"test_run_{RUN_TIMESTAMP}")

if not os.path.exists(TEST_RUN_DIR):
    os.makedirs(TEST_RUN_DIR)


@pytest.fixture(scope="function")
def driver(request):
    """Фікстура для налаштування WebDriver"""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.base_url = read_config.get_url()

    # Отримуємо ім'я тестового файлу
    test_file_name = os.path.splitext(os.path.basename(request.node.fspath))[0]
    test_name = request.node.name
    test_file_dir = os.path.join(TEST_RUN_DIR, f"{test_file_name}_{RUN_TIMESTAMP}")

    # Зберігаємо ці дані у globals
    globals.test_file_dir = test_file_dir
    globals.test_name = test_name

    # Створюємо папку для тестів, якщо її немає
    if not os.path.exists(test_file_dir):
        os.makedirs(test_file_dir)

    # Ініціалізація глобального логера
    log_file_name = f"{test_name}_{RUN_TIMESTAMP}.log"
    initialize_logger(log_file_name, test_file_dir)

    # Логування початку тесту
    logger = Logger.get_global_logger()
    logger.info(f"Starting test: {request.node.nodeid}")

    yield driver

    # Логування завершення тесту
    logger.info(f"Test {request.node.nodeid} finished")
    Logger.log_test_summary()
    driver.quit()


def pytest_runtest_teardown(item):
    """Обробка помилок після завершення тесту."""
    if globals.list_exceptions:
        pytest.fail(f"Test failed after execution: {item.name}", pytrace=False)

def pytest_runtest_makereport(item, call):
    """Зберігає скріншоти у разі помилки."""
    if call.when == "call" and call.excinfo is not None:
        if str(call.excinfo.value) != f"Test failed after execution: {item.name}":
            if 'driver' in item.funcargs:
                driver = item.funcargs['driver']
                Logger.save_screenshot(driver)

