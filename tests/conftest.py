import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger, initialize_logger
from utils import read_config
from utils import globals

# Створення загальної папки для запуску тестів
RUN_TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
TEST_RUN_DIR = os.path.join("reports", f"test_run_{RUN_TIMESTAMP}")

if not os.path.exists(TEST_RUN_DIR):
    os.makedirs(TEST_RUN_DIR)


@pytest.fixture(scope="function")
def driver(request):
    """Фікстура для налаштування WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.base_url = read_config.get_url()

    # Отримуємо ім'я тестового файлу
    test_file_name = os.path.splitext(os.path.basename(request.node.fspath))[0]  # Ім'я без розширення
    test_name = request.node.name  # Назва тесту
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Створюємо папку для тестового файлу всередині test_run
    test_file_dir = os.path.join(TEST_RUN_DIR, f"{test_file_name}_{RUN_TIMESTAMP}")
    if not os.path.exists(test_file_dir):
        os.makedirs(test_file_dir)

    # Ініціалізація глобального логера
    log_file_name = f"{test_name}_{timestamp}.log"  # Лог-файл для конкретного тесту
    initialize_logger(log_file_name, test_file_dir)

    # Логування початку тесту
    logger = Logger.get_global_logger()
    logger.info(f"Starting test: {request.node.nodeid}")

    yield driver

    # Логування завершення тесту
    logger.info(f"Test {request.node.nodeid} finished")
    Logger.log_test_summary()
    driver.quit()


def pytest_runtest_makereport(item, call):
    """Обробка помилок і збереження скріншотів у разі неуспіху"""
    if call.excinfo is not None:  # Якщо є помилка в тесті
        if 'driver' in item.funcargs:
            logger = Logger.get_global_logger()
            driver = item.funcargs['driver']

            globals.list_exceptions.append([call.excinfo.type, call.excinfo.value])

            test_file_name = os.path.splitext(os.path.basename(item.fspath))[0]  # Ім'я тестового файлу
            test_name = item.name  # Назва тесту
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            # Директорія для скріншотів
            test_file_dir = os.path.join(TEST_RUN_DIR, f"{test_file_name}_{RUN_TIMESTAMP}")
            screenshot_name = f"{test_name}_{timestamp}.png"

            # Збереження скріншоту
            Logger.save_screenshot(driver, test_file_dir, screenshot_name)
            logger.error(f"Test {item.nodeid} failed with {call.excinfo}")
