from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        # self.register_new_user()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "login" in url, "URL does not contain 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        reg_email.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASS1)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASS2)
        pass1.send_keys(password)
        pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON)
        button.click()