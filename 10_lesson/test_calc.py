from calc_page import Calculator_page
import allure


@allure.title("Тестирование калькулятора")
@allure.description(
    "Проверка калькулятора при выполнении сложения двух цифр"
    "и ожидания появления верного результата в поле ответа"
)
@allure.feature("Операция сложения")
@allure.severity(allure.severity_level.TRIVIAL)
def test_calculator(driver) -> None:
    page = Calculator_page(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open_page()

    with allure.step("Очистка поля ввода и ввод нового значения (45 секунд)"):
        page.enter_delay_value("45")

    with allure.step("Клик на цифру 7"):
        page.click_seven()

    with allure.step("Клик на знак +"):
        page.click_plus()

    with allure.step("Клик на цифру 8"):
        page.click_eight()

    with allure.step("Клик на знак ="):
        page.click_equal()

    with allure.step("Ожидание результата 15 в поле ответа"):
        page.wait_for_result_text("15")
