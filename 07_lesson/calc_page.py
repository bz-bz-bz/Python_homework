from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator_page:
    def __init__(self, driver):
        self.driver = driver
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.SCREEN_RESULT = (By.CSS_SELECTOR, ".screen")
        self.BTN_7 = (By.XPATH, "//span[text()='7']")
        self.BTN_PLUS = (By.XPATH, "//span[text()='+']")
        self.BTN_8 = (By.XPATH, "//span[text()='8']")
        self.BTN_EQUAL = (By.XPATH, "//span[text()='=']")

    def open_page(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/"
                        "slow-calculator.html"
                        )

    def enter_delay_value(self, seconds: str):
        input_field = self.driver.find_element(*self.DELAY_INPUT)
        input_field.clear()
        input_field.send_keys(seconds)

    def click_seven(self):
        self.driver.find_element(*self.BTN_7).click()

    def click_plus(self):
        self.driver.find_element(*self.BTN_PLUS).click()

    def click_eight(self):
        self.driver.find_element(*self.BTN_8).click()

    def click_equal(self):
        self.driver.find_element(*self.BTN_EQUAL).click()

    def wait_for_result_text(self, expected_text: str):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.SCREEN_RESULT, expected_text)
        )
