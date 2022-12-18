from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_item_name_in_message(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def get_item_price_in_message(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_MESSAGE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

