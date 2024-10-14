from selenium.webdriver.common.by import By
class ConfirmPage:
    countryInbox = (By.ID, "country")
    acceptTerms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[value='Purchase']")
    successPurchaseMessage = (By.CLASS_NAME, "alert-success")
    spainOptionButton = (By.XPATH, "//a[normalize-space()='Spain']")
    def __init__(self,driver):
        self.driver = driver

    def getCountryInbox (self):
        return self.driver.find_element(*ConfirmPage.countryInbox)

    def getTerms (self):
        return self.driver.find_element(*ConfirmPage.acceptTerms)

    def getPurchaseButton (self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessPurchaseMessage (self):
        return self.driver.find_element(*ConfirmPage.successPurchaseMessage)

    def getsSpainOptionButton(self):
        return self.driver.find_element(*ConfirmPage.spainOptionButton)