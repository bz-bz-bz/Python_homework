from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Information_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTIUNE = (By.ID, "contiune")

    def firstname(self, firstname: str):
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)

    def lastname(self, lastname: str):
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)

    def postal_code(self, postal_code: str):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def contiune_bttn(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTIUNE)).click()

    def full_info_form(self, firstname: str, lastname: str, postal_code: str):
        self.firstname(firstname)
        self.lastname(lastname)
        self.postal_code(postal_code)
        self.contiune_bttn()
