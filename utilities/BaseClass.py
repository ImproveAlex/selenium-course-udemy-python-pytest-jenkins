import logging
import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_xpath_presence(self, xpath):
        wait = WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def verify_class_presence(self, class_name):
        wait = WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))

    def select_dropdown_by_id(self, dropdown_id, index):
        """
        Select an option from a dropdown by index.

        :param dropdown_id: The ID of the dropdown element.
        :param index: The index of the option to select (0-based).
        """
        dropdown = Select(self.driver.find_element(By.ID, dropdown_id))
        dropdown.select_by_index(index)
        return dropdown.first_selected_option.text  # Return the text of the selected option

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger