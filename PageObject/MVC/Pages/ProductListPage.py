import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from PageObject.BaseApp import BasePage


class ProductListLocators:
    loc_btn_close_dialog = (By.CSS_SELECTOR, "button.closeModal")
    loc_dialog = (By.CSS_SELECTOR, "section.MegaUI__modal-body")


class ProductListHelper(BasePage):
    def check_visibility_dialog(self):
        time.sleep(5)
        try:
            self.find_element(ProductListLocators.loc_dialog)
        except TimeoutException:
            return False
        return True

    def close_dialog(self):
        elm = self.find_element(ProductListLocators.loc_btn_close_dialog)
        elm.click()
