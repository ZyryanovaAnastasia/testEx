import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome('../../../chromedriver')
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def browserMVC():
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "Galaxy S5"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options, executable_path='../../../chromedriver')
    yield driver
    driver.quit()
