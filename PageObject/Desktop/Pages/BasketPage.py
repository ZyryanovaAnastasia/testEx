from selenium.webdriver.common.by import By
from PageObject.BaseApp import BasePage


class BasketLocators:
    loc_all_items_list = (By.CSS_SELECTOR, "ul.cart-list > li")


class BasketHelper(BasePage):
    def check_count_product(self, expected_count):
        count = len(self.find_elements(BasketLocators.loc_all_items_list))
        assert count == expected_count
