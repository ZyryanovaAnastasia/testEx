import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.ennergiia.com/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_random_item_from_all(self, loc_all_elements):
        all_elements = self.find_elements(loc_all_elements)
        random_elm = all_elements[random.randint(0, len(all_elements) - 1)]
        random_elm.click()

    def check_visible_elm(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def perform_element(self, locator):
        elm = self.find_element(locator)
        ActionChains(self.driver).move_to_element(elm).perform()

    def change_locator(self, locator, name):
        new_locator = [locator[0], locator[1].replace('<name>', name)]
        return new_locator
