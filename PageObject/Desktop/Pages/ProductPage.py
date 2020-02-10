from selenium.webdriver.common.by import By
from PageObject.BaseApp import BasePage


class ProductLocators:
    loc_btn_add_favorites = (By.CSS_SELECTOR, "button.wishlist-add-button")
    loc_btn_add_basket = (By.XPATH, "//button[text()='Добавить в корзину']")


class ProductHelper(BasePage):
    def add_in_favorites(self):
        elm = self.find_element(ProductLocators.loc_btn_add_favorites)
        elm.click()

    def add_in_basket(self):
        elm = self.find_element(ProductLocators.loc_btn_add_basket)
        elm.click()
