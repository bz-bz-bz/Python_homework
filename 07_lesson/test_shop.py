from auth_page import Auth_Page
from shop_page import Shop_Page
from basket_page import Basket_Page
from info_page import Information_Page
from price import Price_total


def test_shop(driver):
    page = Auth_Page(driver)
    page.open_page()
    page.login("standard_user", "secret_sauce")
    shop_page = Shop_Page(driver)
    shop_page.add_products()
    basket_page = Basket_Page(driver)
    basket_page.click_checkout()
    info_page = Information_Page(driver)
    info_page.fill_info_form("Мария", "Канцирева", "188300")
    overview_page = Price_total(driver)
    assert overview_page.get_total_price_text() == "Total: $58.29"
    overview_page.click_finish()
