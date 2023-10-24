from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message(self, expected_message):
        message_from_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert expected_message in message_from_basket, "Отутствует сообщение"