from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    BASKET_PAGE_URL = "http://selenium1py.pythonanywhere.com/basket/"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), "Basket has items"

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Basket is empty message is not presented"
