from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_login_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "basket" in url, "URL does not contain 'basket'"

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        login_link.click()

    def check_that_basket_is_empty(self):
        # print(self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text.split(".")[0])
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text.split(".")[0] == False, \
            "Basket is not empty"
        
    def basked_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
        "Basket should be empty, but it's not"