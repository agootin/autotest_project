import time

import pytest

from src.pages.basket_page import BasketPage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        random_email = str(time.time()) + "@fakemail.org"
        random_password = str(time.time()) + "111111111"
        page = LoginPage(browser, url=LoginPage.LOGIN_PAGE_URL)
        page.open()
        page.register_new_user(random_email, random_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
        page.open()
        page.add_item_to_cart()
        assert page.get_item_name_in_message() == page.get_item_name(), "Item name in message is wrong"
        assert page.get_item_price_in_message() == page.get_item_price(), "Item price in message is wrong"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('promo', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo):
    link = ProductPage.PRODUCT_PAGE_URL +"?promo=offer/" + str(promo)
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    assert page.get_item_name_in_message() == page.get_item_name(), "Item name in message is wrong"
    assert page.get_item_price_in_message() == page.get_item_price(), "Item price in message is wrong"


@pytest.mark.xfail(reason="negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.add_item_to_cart()
    page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, url=ProductPage.PRODUCT_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_basket_is_empty_message()
