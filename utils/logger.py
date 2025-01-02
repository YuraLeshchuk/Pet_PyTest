import logging
import os
from datetime import datetime
from utils import globals

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class Logger:
    """
    Клас для управління логуванням і збереженням скріншотів для тестів.
    """

    @staticmethod
    def setup_logger(test_name: str, logs_dir: str) -> logging.Logger:
        """
        Налаштовує окремий логер для кожного тесту.

        :param test_name: Назва тесту (ім'я функції тесту).
        :param logs_dir: Директорія, де зберігатимуться лог-файли.
        :return: Логер, налаштований для конкретного тесту.
        """
        os.makedirs(logs_dir, exist_ok=True)

        log_file = os.path.join(logs_dir, f"{test_name}_{timestamp}.log")

        logger = logging.getLogger(test_name)
        logger.setLevel(logging.DEBUG)

        # Видалення старих хендлерів
        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)

        # Додавання FileHandler
        file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger


    @staticmethod
    def step(step_number: str, description: str):
        """
        Логування кроків тесту у форматі 'STEP X: description'.
        """
        msg = f"STEP {step_number} : {description} "
        while len(msg) < 55:
            msg += "*"
        try:
            logging.info(msg)
        except Exception:
            logging.exception("Log step failed")

    @staticmethod
    def checkpoint(message: str):
        """
        Логування кроків тесту у форматі 'STEP X: description'.
        """

        logging.info(f" CHECKPOINT: {message}")
        globals.list_checkpoints.append(message)
    @staticmethod
    def test_summary():
        logging.info("*************************************************")
        logging.info("****************** TEST SUMMARY *****************")
        logging.info("*************************************************")
        logging.info(" CHECKPOINTS: " + str(len(globals.list_checkpoints)))
        # logging.info(" WARNINGS: " + globals.int_total_warnings)
        # logging.info(" ERRORS: " + globals.int_total_errors)
        # logging.info(" EXCEPTIONS: " + globals.int_total_exceptions)

    @staticmethod
    def save_screenshot(driver, test_dir: str, test_name: str):
        """
        Зберігає скріншот у папці конкретного тесту.

        :param driver: WebDriver, який використовується у тесті.
        :param test_dir: Директорія для збереження скріншота.
        :param test_name: Назва тесту.
        :param timestamp: Час створення скріншота.
        """
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(test_dir, screenshot_name)

        try:
            driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved at: {screenshot_path}")
        except Exception as e:
            logging.error(f"Failed to save screenshot: {e}")
