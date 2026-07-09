from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Price_total:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.TOTAL_PRICE_LABEL = (By.CLASS_NAME, "summary_total_label")
        self.FINISH_BUTTON = (By.ID, "finish")

    def get_total_price_text(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE_LABEL))
        return element.text

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
