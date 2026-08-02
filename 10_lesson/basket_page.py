from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basket_Page:
    """Класс для взаимодействия с корзиной"""

    def __init__(self, driver) -> None:
        """Инициализация драйвера и поиск элемента на странице
        return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """Ожидание кликабельности элемента,
        после того, как элемент становится кликабельным,
        осуществляется клик на него
        Исключая self, у метода нет параметров
        return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
