from selenium.webdriver.common.by import By


class TestShopPage:
    def test_add_to_basket_button_is_displayed(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        add_to_basket_btn = browser.find_element(By.CSS_SELECTOR, ".add-to-basket")
        assert add_to_basket_btn.is_displayed(), "Кнопка не отображается"
