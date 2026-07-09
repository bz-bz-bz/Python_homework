from calc_page import Calculator_page


def test_calculator(driver):
    page = Calculator_page(driver)
    page.open_page()
    page.enter_delay_value("45")
    page.click_seven()
    page.click_plus()
    page.click_eight()
    page.click_equal()

    page.wait_for_result_text("15")
