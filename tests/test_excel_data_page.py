import pytest
from pageObjects.ExcelDataPage import ExcelDataPage
from utilities.BaseClass import BaseClass


class TestExcelDataPage(BaseClass):
    def download_file(self):
        log = self.getLogger()
        excel_data_page = ExcelDataPage(self.driver)
        excel_data_page.get_download_button().click()