import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from testData.excelTests import ExcelTestData
from utilities.BaseClass import BaseClass




class TestHomePage(BaseClass):
    @pytest.fixture(params= ExcelTestData.getTestData())
    def get_home_page_data(self, request):
        return request.param
    def test_form_submission(self, get_home_page_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getEmailInput().send_keys(get_home_page_data["email"])
        homepage.getPasswordInput().send_keys(get_home_page_data["password"])
        homepage.getIceCreamCheckbox().click()
        homepage.getNameInput().send_keys(get_home_page_data["firstname"])
        log.info(f"Testing with user: {get_home_page_data["firstname"]}")
        homepage.getStudentInput().click()
        #Static Dropdown
        selected_option_text = self.select_dropdown_by_id("exampleFormControlSelect1", int(get_home_page_data["index"]))
        assert selected_option_text == get_home_page_data["gender"]
        homepage.getbDayInput().send_keys(get_home_page_data["bday"])
        homepage.getSubmitButton().click()
        homepage.getStudentInput().click()
        message = homepage.getSuccessMsg().text
        log.info(message)
        assert "Success" in message
        homepage.getTwoWayData().send_keys(get_home_page_data["two_way"])
        homepage.getTwoWayData().clear()
        self.driver.refresh()