import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepPage = HomePage(self.driver)
        checkoutPage = homepPage.shopItems()
        log.info("We have added item to shoping cart")
        products = checkoutPage.getProducts()
        for product in products:
            log.info(f"Products found:{checkoutPage.getProductTile(product)}")
            if checkoutPage.getProductTile(product) == "Blackberry":
                checkoutPage.addProductToCart(product).click()
                checkoutPage.getCheckoutButton().click()
                confirmPage = checkoutPage.getFinalCheckoutButton()
                confirmPage.getCountryInbox().send_keys("spain")
                log.info("Searching for spain")
                self.verify_xpath_presence("//a[normalize-space()='Spain']")
                action = ActionChains(self.driver)
                action.move_to_element(
                    confirmPage.getsSpainOptionButton()).click().perform()

                confirmPage.getTerms().click()
                confirmPage.getPurchaseButton().click()

                self.verify_class_presence( "alert-success")
                assert "Success!" in confirmPage.getSuccessPurchaseMessage().text
                log.info("Purchase Successful")