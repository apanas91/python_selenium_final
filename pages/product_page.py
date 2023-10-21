from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_added(self, product_name):
        prod_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert prod_name == product_name, "Имя товара не соответствет"

    def should_be_basket_amount(self, amount):
        am = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).text
        assert amount in am, "Сумма товара в корзине не совпадает"

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_amount(self):
        amount = self.browser.find_element(*ProductPageLocators.PRODUCT_AMOUNT).text
        return amount
