from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    ITEM_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
