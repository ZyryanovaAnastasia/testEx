import time

from selenium.webdriver.common.by import By
from PageObject.BaseApp import BasePage


class ProductListLocators:
    loc_all_items_subcategory = (By.CSS_SELECTOR, "div.category-item > * > div.category-item")
    loc_any_item_subcategory = (By.XPATH, "//span[contains(text(), '<name>')]")
    loc_all_items_category = (By.XPATH, '//div[@class="categories-list"]/div')
    loc_product_brand = (By.CLASS_NAME, "product-preview__brand")
    first_block_in_list_css = (By.CSS_SELECTOR, "div.product-list__items > div:first-child")


class ProductListHelper(BasePage):
    def choose_random_subcategory(self):
        self.perform_product_brand()
        self.click_random_item_from_all(ProductListLocators.loc_all_items_subcategory)

    def click_subcategory_with_name(self, name):
        self.perform_product_brand()
        loc = self.change_locator(ProductListLocators.loc_any_item_subcategory, name)
        elm = self.find_element(loc)
        elm.click()

    def perform_product_brand(self):
        self.perform_element(ProductListLocators.loc_product_brand)

    def open_first_product(self):
        time.sleep(5)
        elm = self.find_element(ProductListLocators.first_block_in_list_css)
        elm.click()
