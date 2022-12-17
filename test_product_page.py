import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(promo)
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    assert page.get_item_name_in_message() == page.get_item_name(), "Item name in message is wrong"
    assert page.get_item_price_in_message() == page.get_item_price(), "Item price in message is wrong"
