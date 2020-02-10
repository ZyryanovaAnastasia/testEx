import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from PageObject.BaseApp import BasePage


class MenuDesktopLocators:
    loc_btn_confirm_geolocation = (By.CSS_SELECTOR, "button.geolocation-popup__btn_primary")
    loc_btn_change_geolocation = (By.CSS_SELECTOR, "button.geolocation-popup__btn_secondary")
    loc_logo_desktop = (By.CLASS_NAME, "menu-desktop__logo")
    loc_any_item_on_menu = [By.XPATH, "//a[contains(text(), '<name>')]"]
    loc_all_section = (By.CSS_SELECTOR, "div.categories-main-menu__root > a")
    loc_all_categories = (By.CSS_SELECTOR, "a.title")
    loc_btn_favorites = (By.CLASS_NAME, "wishlist__icon")
    loc_btn_basket = (By.CLASS_NAME, "cart-popup__wrapper")
    loc_badge_in_basket = (By.CSS_SELECTOR, "div.badge > span")


class MenuDesktopHelper(BasePage):
    def open_main(self):
        self.go_to_site()

    def select_geolocation_window(self, option):
        if option == "confirm":
            btn_confirm = self.find_element(MenuDesktopLocators.loc_btn_confirm_geolocation)
            btn_confirm.click()
        elif option == "change":
            btn_change = self.find_element(MenuDesktopLocators.loc_btn_change_geolocation)
            btn_change.click()

    def click_btn_favorites(self):
        btn_favorites = self.find_element(MenuDesktopLocators.loc_btn_favorites)
        btn_favorites.click()

    def check_count_badge_basket(self, expected_count):
        count = self.find_element(MenuDesktopLocators.loc_badge_in_basket).text
        assert count == str(expected_count)

    def click_btn_basket(self):
        btn_basket = self.find_element(MenuDesktopLocators.loc_btn_basket)
        btn_basket.click()

    def choose_random_section(self, last_value):
        all_selection = self.find_elements(MenuDesktopLocators.loc_all_section)
        random_elm = all_selection[random.randint(0, last_value)]
        ActionChains(self.driver).move_to_element(random_elm).perform()

    def perform_section_with_name(self, name):
        loc = self.change_locator(MenuDesktopLocators.loc_any_item_on_menu, name)
        self.perform_element(self.change_locator(MenuDesktopLocators.loc_any_item_on_menu, name))

    def click_category_with_name(self, name):
        loc = self.change_locator(MenuDesktopLocators.loc_any_item_on_menu, name)
        elm = self.find_element(loc)
        elm.click()

    def choose_random_category(self):
        self.click_random_item_from_all(MenuDesktopLocators.loc_all_categories)

    def check_badge_basket_visibility(self):
        try:
            self.find_element(MenuDesktopLocators.loc_badge_in_basket)
        except TimeoutException:
            return False
        return True
