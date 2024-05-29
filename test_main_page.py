# pytest -v --tb=line --language=en test_main_page.py
# pytest -v test_main_page.py
# pytest -v -s -m login_guest test_main_page.py

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                                         # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, link)
    basket_page.go_to_basket_page()
    basket_page.should_be_basket_url()
    basket_page.check_that_basket_is_empty()
    basket_page.basked_should_be_empty()