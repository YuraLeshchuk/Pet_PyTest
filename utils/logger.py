import logging
import os
from datetime import datetime


class Logger:
    test_file_dir = None  # Змінна для директорії тестового файлу

    @staticmethod
    def setup_test_file_dir(test_file_name):
        """Створення папки для тестового файлу (один раз)"""
        if Logger.test_file_dir is None:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            Logger.test_file_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "reports")),
                                                f"{test_file_name}_{timestamp}")
            if not os.path.exists(Logger.test_file_dir):
                os.makedirs(Logger.test_file_dir)
        return Logger.test_file_dir

    @staticmethod
    def setup_logger(test_file_name, test_name):
        """Створення папки для конкретного тесту"""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Папка для тестового файлу
        test_file_dir = Logger.setup_test_file_dir(test_file_name)

        # Папка для конкретного тесту
        test_dir = os.path.join(test_file_dir, f"{test_name}_{timestamp}")
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        # Файл логів для конкретного тесту
        log_filename = os.path.join(test_dir, f"{test_name}_{timestamp}.log")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Додаємо FileHandler
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        return logger, test_dir  # Повертаємо logger і директорію для тесту

    @staticmethod
    def log_info(message):
        """Логування інформаційних повідомлень"""
        logging.info(message)

    @staticmethod
    def log_error(message):
        """Логування помилок"""
        logging.error(message)

    @staticmethod
    def step(step_number: str, description):
        msg = "STEP " + step_number + " : " + description + " "
        while len(msg) < 55:
            msg += "*"
        try:
            logging.info(msg)
        except Exception:
            logging.exception("Log step failed")
        pass

    @staticmethod
    def save_screenshot(driver, test_dir, test_name, timestamp):
        """Зберігає скріншот у папці конкретного тесту"""
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(test_dir, screenshot_name)

        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot_path: {screenshot_path}")
