from selenium.webdriver.common.by import By

class ExcelDataPage:
    download_button = (By.ID, "downloadButton")
    file_input_button = (By.ID, "fileinput")

    def __init__(self, driver):
        self.driver = driver

    def get_download_button(self):
        return self.driver.find_element(*ExcelDataPage.download_button)

    def get_file_input_button(self):
        return self.driver.find_element(*ExcelDataPage.file_input_button)