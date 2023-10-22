import time
import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    # product_name = page.get_product_name()
    # amount = page.get_product_amount()
    page.click_add_to_basket_button()
    # page.solve_quiz_and_get_code()
    # time.sleep(180)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    # page.should_be_product_added(product_name)
    # page.should_be_basket_amount(amount)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    page.click_add_to_basket_button()
    # page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

