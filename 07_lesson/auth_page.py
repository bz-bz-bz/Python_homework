from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Auth_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.USERNAME = (By.ID, "user-name")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def username(self, username: str):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def password(self, password: str):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def login_bttn(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username: str, password: str):
        self.username(username)
        self.password(password)
        self.login_bttn()
