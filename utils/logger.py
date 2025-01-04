import logging
import os
from utils import globals

_global_logger = None


def initialize_logger(log_file_name: str, test_file_dir: str):
    """
    Ініціалізація глобального логера.
    """
    global _global_logger
    if not os.path.exists(test_file_dir):
        os.makedirs(test_file_dir)

    _global_logger = logging.getLogger("LOGGER")
    _global_logger.setLevel(logging.INFO)

    # Видаляємо старі хендлери
    if _global_logger.handlers:
        for handler in _global_logger.handlers:
            _global_logger.removeHandler(handler)

    # Додавання FileHandler
    log_file = os.path.join(test_file_dir, log_file_name)
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    _global_logger.addHandler(file_handler)


class Logger:
    @staticmethod
    def get_global_logger() -> logging.Logger:
        if _global_logger is None:
            raise ValueError("Logger is not initialized.")
        return _global_logger

    @staticmethod
    def save_screenshot(driver, test_file_dir, screenshot_name):
        screenshot_path = os.path.join(test_file_dir, screenshot_name)
        driver.save_screenshot(screenshot_path)
        _global_logger.info(f"Screenshot saved at: {screenshot_path}")

    @staticmethod
    def step(step_number: str, description: str):
        """
        Логування кроку тесту у форматі:
        STEP [номер]: опис
        """
        if _global_logger:
            msg = f"STEP {step_number}: {description}"
            _global_logger.info(msg)
        else:
            raise ValueError("Logger is not initialized.")

    @staticmethod
    def checkpoint(msg):
        """

        """
        if _global_logger:
            globals.int_total_checkpoints +=1
            msg = f"CHECKPOINT {str(globals.int_total_checkpoints)}: {msg}"
            _global_logger.info(msg)
        else:
            raise ValueError("Logger is not initialized.")

    @staticmethod
    def error(msg, error_class, **kwargs):
        """

        """
        if _global_logger:
            _global_logger.error(msg)
            globals.list_warnings.append(msg)
            raise error_class
        else:
            raise ValueError("Logger is not initialized.")

    @staticmethod
    def exception(msg):
        if _global_logger:
            _global_logger.exception(msg)
            globals.list_exceptions.append(msg)
        else:
            raise ValueError("Logger is not initialized.")

    @staticmethod
    def log_test_summary():
        """

        """
        _global_logger.info("*******************************************************")
        _global_logger.info("**************** TEST SCENARIO SUMMARY ****************")
        _global_logger.info("*******************************************************")
        _global_logger.info("    TOTAL CHECKPOINTS: " + str(len(globals.list_checkpoints)))
        _global_logger.info("    TOTAL WARNINGS: " + str(len(globals.list_warnings)))
        _global_logger.info("    TOTAL EXCEPTIONS: " + str(len(globals.list_exceptions)))
