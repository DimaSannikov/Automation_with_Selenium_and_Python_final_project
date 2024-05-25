from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1)>.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    SUCCESS_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
