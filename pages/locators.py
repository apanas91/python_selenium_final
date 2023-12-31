from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div .alertinner strong")
    BASKET_AMOUNT = (By.CSS_SELECTOR, "div .alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div .product_main h1")
    PRODUCT_AMOUNT = (By.CSS_SELECTOR, "div .product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner :nth-child(1)")

class BasketPageLocators:
    BASKET_FORM = (By.ID, "basket_formset")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")