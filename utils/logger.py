import datetime
import logging
import os
from utils import globals


class Logger:

    @staticmethod
    def setup_loger(test_name):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_dir = os.path.join("../reports", f"{test_name}_{timestamp}")
        log_filename = os.path.join(report_dir, f"{test_name}_{timestamp}.log")

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(logging.Formatter())

        logger.addHandler(file_handler)
        return logger

    @staticmethod
    def info(message):
        logging.info(message)








    @staticmethod
    def scenario_start(test_name):
        """
        Adds a test method start statement to the log files.

        .. function:: logger_scenario_start

            :param test_method_name:
            :type test_method_name: str

        Examples:
        >>> logger.logger_scenario_start(testMethodName)
        """
        logging.info("*******************************************************")
        logging.info("**************** TEST SCENARIO START ******************")
        logging.info("*******************************************************")
        logging.info("**************** Test Name: " + str(test_name))
        logging.info("*******************************************************")

    @staticmethod
    def scenario_summary(**kwargs):
        skipped = kwargs.get('skipped', False)
        name = kwargs.get('name', "")

        logging.info("*******************************************************")
        logging.info("**************** TEST SCENARIO SUMMARY ****************")
        logging.info("*******************************************************")

        if not skipped:
            logging.info("    int_total_checkpoints: " +
                    str(globals.int_total_checkpoints))
            logging.info("    int_total_warnings: " +
                    str(globals.int_total_warnings))
            logging.info("    int_total_errors: " + str(globals.int_total_errors))
            logging.info("    int_total_exceptions: " +
                    str(globals.int_total_exceptions))
        else:
            logging.info("This method has been skipped: " + name)
        logging.info("*******************************************************")
