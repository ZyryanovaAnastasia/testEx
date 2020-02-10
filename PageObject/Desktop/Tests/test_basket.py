from pytest_bdd import scenarios, when, then
from PageObject.Desktop.Pages.Elements.MenuDesktopElm import MenuDesktopHelper
from PageObject.Desktop.Pages.ProductListPage import ProductListHelper
from PageObject.Desktop.Pages.ProductPage import ProductHelper
from PageObject.Desktop.Pages.BasketPage import BasketHelper

scenarios('../Feature/basket.feature')


@when('открывается главная страница')
def open_main(browser):
    MenuDesktopHelper(browser).go_to_site()


@when('подтверждение геолокации')
def geolocation_confirmation(browser):
    MenuDesktopHelper(browser).select_geolocation_window("confirm")


@when('счётчик корзины отсутствует')
def no_basket_counter(browser):
    assert MenuDesktopHelper(browser).check_badge_basket_visibility() is False


@when('выбран раздел <section>')
def selected_section(browser, section):
    MenuDesktopHelper(browser).perform_section_with_name(section)


@when('выбрана категория <category>')
def selected_category(browser, category):
    MenuDesktopHelper(browser).click_category_with_name(category)


@when('выбрана подкатегория <subcategory>')
def selected_subcategory(browser, subcategory):
    ProductListHelper(browser).click_subcategory_with_name(subcategory)


@when('добавляется любой случайный товар в корзину')
def add_product(browser):
    ProductListHelper(browser).open_first_product()
    ProductHelper(browser).add_in_basket()


@when('совершается переход в корзину')
def go_in_basket(browser):
    MenuDesktopHelper(browser).click_btn_basket()


@then('в корзине 1 товар')
def one_product_in_basket(browser):
    MenuDesktopHelper(browser).check_count_badge_basket(1)
    BasketHelper(browser).check_count_product(1)
