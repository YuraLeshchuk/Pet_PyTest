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
    """
    Фікстура для налаштування WebDriver.
    """
    # Налаштування WebDriver
    options = webdriver.ChromeOptions()
    if read_config.driver_mode() == "true":
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.base_url = read_config.get_url()

    # Отримання інформації про тестовий файл і тест
    test_file_name = os.path.basename(request.node.fspath).split('.')[0]  # Ім'я тестового файлу без розширення
    test_name = request.node.name  # Назва тесту
    timestamp = request.config._timestamp  # Використовуємо загальний timestamp для всіх тестів

    # Створення загальної папки для логів тестового файлу
    logs_dir = os.path.join("reports", f"{test_file_name}_{timestamp}")
    os.makedirs(logs_dir, exist_ok=True)

    # Налаштування логера
    logger = Logger.setup_logger(test_name, logs_dir)

    # Зберігання інформації в driver
    driver._logger = logger
    driver._test_dir = logs_dir
    driver._test_name = test_name

    logger.info(f"Starting test: {request.node.nodeid}")

    try:
        yield driver
    finally:
        logger.info(f"Finishing test: {request.node.nodeid}")
        driver.quit()

        # Закриття всіх хендлерів логера
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)


def pytest_sessionstart(session):
    """
    Ініціалізує timestamp для всього тестового запуску.
    """
    session.config._timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


def pytest_runtest_makereport(item, call):
    """
    Обробка результатів тесту та збереження скріншотів у разі помилок.
    """
    if call.when == "call" and call.excinfo is not None:  # Виконання тесту завершилося помилкою
        driver = item.funcargs.get("driver", None)
        if driver:
            test_dir = driver._test_dir
            test_name = driver._test_name

            # Збереження скріншота та логування
            Logger.save_screenshot(driver, test_dir, test_name)
            driver._logger.error(f"Test {item.nodeid} failed with: {call.excinfo}")
