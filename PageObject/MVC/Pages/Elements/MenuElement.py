import time

from selenium.webdriver.common.by import By
from PageObject.BaseApp import BasePage


class MenuLocators:
    loc_side_bar = (By.XPATH, "//*[@data-test='navSideBar']")
    loc_any_section = (By.XPATH, "//*[@data-test='hierarchyRoots']/li[@aria-label='<name>']")
    loc_any_category = (By.XPATH, "//*[@data-test='hierarchyItemName'][ .='<name>']")
    loc_any_subcategory = (By.XPATH, "//button[@data-test='hierarchyItemTrigger'][@aria-label='<name>']")


class MenuHelper(BasePage):
    def click_side_bar(self):
        elm = self.find_element(MenuLocators.loc_side_bar)
        elm.click()
        time.sleep(5)

    def click_section_with_name(self, name):
        loc = self.change_locator(MenuLocators.loc_any_section, name)
        elm = self.find_element(loc)
        elm.click()
        time.sleep(5)

    def click_category_with_name(self, name):
        loc = self.change_locator(MenuLocators.loc_any_category, name)
        self.perform_element(loc)
        elm = self.find_element(loc)
        elm.click()

    def click_subcategory_with_name(self, name):
        loc = self.change_locator(MenuLocators.loc_any_subcategory, name)
        self.perform_element(loc)
        elm = self.find_element(loc)
        elm.click()