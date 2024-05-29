from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1)>.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    SUCCESS_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > .basket-title.hidden-xs")
