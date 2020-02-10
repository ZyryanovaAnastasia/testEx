from selenium.webdriver.common.by import By
from PageObject.BaseApp import BasePage


class WishlistLocators:
    loc_h3_list_favorites = (By.CSS_SELECTOR, "ul.wishlist-product-list > h3")
    loc_all_items_list = (By.CSS_SELECTOR, "ul.wishlist-product-list > li")


class WishlistHelper(BasePage):
    def check_availability_product_in_list(self):
        text_favorites_list = self.find_element(WishlistLocators.loc_h3_list_favorites).text
        assert text_favorites_list == "Список желаемого пуст"

    def check_count_product(self, expected_count):
        count = len(self.find_elements(WishlistLocators.loc_all_items_list))
        assert count == expected_count
