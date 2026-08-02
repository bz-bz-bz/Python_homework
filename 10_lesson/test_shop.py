from auth_page import Auth_Page
from shop_page import Shop_Page
from basket_page import Basket_Page
from info_page import Information_Page
from price import Price_total
import allure


@allure.title("Тестирование интернет-магазина")
@allure.description(
    "Проверка работы страницы авторизации, страницы с товарами, корзины,"
    "страницы для заполнения личных данных и отбражение верной финальной цены"
)
@allure.feature("Создание заказа")
@allure.severity(allure.severity_level.TRIVIAL)
def test_shop(driver) -> None:
    page = Auth_Page(driver)
    with allure.step("Открытие страницы авторизации"):
        page.open_page()

    with allure.step("Ввод логина standard_user и пароля secret_sauce"):
        page.login("standard_user", "secret_sauce")

    shop_page = Shop_Page(driver)

    with allure.step("Добавленеи товаров в корзину"):
        shop_page.add_products()

    basket_page = Basket_Page(driver)

    with allure.step("Клик по кнопке checkout"):
        basket_page.click_checkout()

    info_page = Information_Page(driver)

    with allure.step("Заполнение полей firstname, lastname, postal_code "):
        info_page.fill_info_form("Мария", "Канцирева", "188300")

    overview_page = Price_total(driver)

    with allure.step("Проверка итоговой стоимости"):
        assert overview_page.get_total_price_text() == "Total: $58.29"

    with allure.step("Клик на кнопку finish и завершение заказа"):
        overview_page.click_finish()
