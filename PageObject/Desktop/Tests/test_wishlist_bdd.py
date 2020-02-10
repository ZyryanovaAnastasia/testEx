from pytest_bdd import scenarios, when, then
from PageObject.Desktop.Pages.Elements.MenuDesktopElm import MenuDesktopHelper
from PageObject.Desktop.Pages.ProductListPage import ProductListHelper
from PageObject.Desktop.Pages.WishlistPage import WishlistHelper
from PageObject.Desktop.Pages.ProductPage import ProductHelper

scenarios('../Feature/wishlist.feature')


@when('открывается главная страница')
@when('совершен переход на главную страницу')
def open_main(browser):
    MenuDesktopHelper(browser).go_to_site()


@when('подтверждение геолокации')
def no_basket_counter(browser):
    MenuDesktopHelper(browser).select_geolocation_window("confirm")


@when('совершён переход в Избранное')
def selected_section(browser):
    MenuDesktopHelper(browser).click_btn_favorites()


@when('список товаров в вишлисте пуст')
def selected_category(browser):
    WishlistHelper(browser).check_availability_product_in_list()


@when('выбран случайный раздел')
def selected_section(browser):
    MenuDesktopHelper(browser).choose_random_section(4)


@when('выбрана случайна категория')
def selected_category(browser):
    MenuDesktopHelper(browser).choose_random_category()


@when('выбрана случайна подкатегория')
def selected_subcategory(browser):
    ProductListHelper(browser).choose_random_subcategory()


@when('открыта любая карточка товара')
def one_product_in_basket(browser):
    ProductListHelper(browser).open_first_product()


@when('товар добавлен в вишлист')
def one_product_in_basket(browser):
    ProductHelper(browser).add_in_favorites()


@then('в вишлисте находится 1 товар')
def one_product_in_basket(browser):
    WishlistHelper(browser).check_count_product(1)
