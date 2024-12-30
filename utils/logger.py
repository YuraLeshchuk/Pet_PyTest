import logging
import os
from datetime import datetime


class Logger:

    @staticmethod
    def setup_logger(test_name):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_dir = os.path.join("../reports", f"{test_name}_{timestamp}")
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

        log_filename = os.path.join(report_dir, f"{test_name}_{timestamp}.log")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        return logger, report_dir

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def save_screenshot(driver, report_dir, test_name):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshot_{test_name}_{timestamp}.png"

        screenshot_path = os.path.join(report_dir, screenshot_name)
        driver.save_screenshot(screenshot_path)
