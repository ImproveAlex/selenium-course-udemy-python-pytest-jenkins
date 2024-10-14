from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    products = (By.XPATH, "//div[@class='card h-100']")
    productTitle = (By.CSS_SELECTOR, "h4[class='card-title'] a")
    productAddToCartButton = (By.CSS_SELECTOR, "div[class='card-footer'] button")
    checkoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    finalCheckoutButton = (By.XPATH, "//button[normalize-space()='Checkout']")
    def __init__(self,driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductTile (self, product):
        return product.find_element(*CheckoutPage.productTitle).text

    def addProductToCart (self, product):
        return product.find_element(*CheckoutPage.productAddToCartButton)

    def getCheckoutButton(self):
        return  self.driver.find_element(*CheckoutPage.checkoutButton)

    def getFinalCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.finalCheckoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage