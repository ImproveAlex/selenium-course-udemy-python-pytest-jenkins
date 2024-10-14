from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.XPATH, "//a[normalize-space()='Shop']")
    emailInput = (By.NAME, "email")
    nameInput =  (By.NAME, "name")
    passwordInput = (By.ID, "exampleInputPassword1")
    iceCreamCheckbox = (By.XPATH, "//input[@id='exampleCheck1']")
    studentInput = (By.ID, "inlineRadio1")
    bDayInput = (By.NAME, "bday")
    submitButton = (By.XPATH, "//input[@type='submit']")
    twoWayData = (By.XPATH,"(//input[@type='text'])[3]")
    successMsg = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getEmailInput(self):
        return self.driver.find_element(*HomePage.emailInput)

    def getNameInput(self):
        return self.driver.find_element(*HomePage.nameInput)

    def getPasswordInput(self):
        return self.driver.find_element(*HomePage.passwordInput)

    def getIceCreamCheckbox(self):
        return self.driver.find_element(*HomePage.iceCreamCheckbox)

    def getStudentInput(self):
        return self.driver.find_element(*HomePage.studentInput)

    def getbDayInput(self):
        return self.driver.find_element(*HomePage.bDayInput)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getTwoWayData(self):
        return self.driver.find_element(*HomePage.twoWayData)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)