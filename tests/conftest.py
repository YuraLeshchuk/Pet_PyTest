import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger
from utils import read_config


@pytest.fixture(scope="function")
def driver(request):
    """Фікстура для налаштування WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.base_url = read_config.get_url()

    # Отримуємо ім'я тестового файлу та тесту
    test_file_name = os.path.basename(request.node.fspath)  # Ім'я тестового файлу
    test_name = request.node.name  # Назва тесту
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Налаштування логування
    logger, test_dir = Logger.setup_logger(test_file_name, test_name)

    # Зберігаємо інформацію для збереження скріншотів
    driver._test_dir = test_dir
    driver._test_name = test_name
    driver._timestamp = timestamp

    Logger.log_info(f"Starting test: {request.node.nodeid}")

    yield driver

    Logger.log_info(f"Test {request.node.nodeid} finished")
    driver.quit()


def pytest_runtest_makereport(item, call):
    """Обробка помилок і збереження скріншотів у разі неуспіху"""
    if call.excinfo is not None:  # Якщо є помилка в тесті
        driver = item.funcargs['driver']
        test_dir = driver._test_dir
        test_name = driver._test_name
        timestamp = driver._timestamp

        Logger.save_screenshot(driver, test_dir, test_name, timestamp)
        Logger.log_info(f"Test {item.nodeid} failed with {call.excinfo}")
