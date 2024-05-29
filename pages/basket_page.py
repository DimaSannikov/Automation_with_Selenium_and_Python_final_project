from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


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
        
    def check_that_empty_basket_contains_text_about_it(self):
        try:
            empty_basket_text = self.browser.find_element(
                *BasketPageLocators.EMPTY_BASKET_TEXT).text.split(".")[0]
            print(f"__{empty_basket_text}__")
        except NoSuchElementException:
            return False
        return True

    def check_that_basket_is_empty(self):
        assert self.check_that_empty_basket_contains_text_about_it(), \
            "Basket is not empty"

    def basked_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
        "Basket should be empty, but it's not"