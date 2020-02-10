import time

from pytest_bdd import scenarios, when, then
from PageObject.MVC.Pages.Elements.MenuElement import MenuHelper
from PageObject.MVC.Pages.ProductListPage import ProductListHelper

scenarios('../Feature/dialog_with_promotional.feature')


@when('открывается главная страница мвс')
def open_main(browserMVC):
    MenuHelper(browserMVC).go_to_site()


@when('выбран раздел <section>')
def open_main(browserMVC, section):
    MenuHelper(browserMVC).click_side_bar()
    MenuHelper(browserMVC).click_section_with_name(section)


@when('выбрана категория <category>')
def open_main(browserMVC, category):
    MenuHelper(browserMVC).click_category_with_name(category)


@when('выбрана подкатегория <subcategory>')
def open_main(browserMVC, subcategory):
    MenuHelper(browserMVC).click_subcategory_with_name(subcategory)


@then('всплывает форма с предложением получить промокод')
def check_dialog_visibility(browserMVC):
    assert ProductListHelper(browserMVC).check_visibility_dialog() is True


@then('данную форму можно закрыть')
def close_dialog(browserMVC):
    ProductListHelper(browserMVC).close_dialog()
