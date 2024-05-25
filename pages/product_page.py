from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def useful_basket_button_should_be_on_the_page(self):
        self.should_be_basket_button()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.success_message_contains_similar_product_name()
        self.success_message_contains_similar_product_price()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not on the page"
    
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is absent"

    def success_message_contains_similar_product_name(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name , "Message contains incorrect product name"

    def success_message_contains_similar_product_price(self):
        product_price_in_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price_in_message == product_price , "Message contains incorrect product price"