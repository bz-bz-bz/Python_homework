from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Shop_Page:
    """Класс для взаимодействия со страницей товаров"""

    def __init__(self, driver) -> None:
        """Инициализация драйвера и поиск элементов на странице
        return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.ADD_SAUCE_LABS = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.BASKET = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def add_tshirt(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.ADD_TSHIRT).click()

    def add_sause_labs(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.ADD_SAUCE_LABS).click()

    def click_basket(self) -> None:
        """Ожидание кликабельности элемента,
        после того, как элемент становится кликабельным,
        осуществляется клик на него
        Исключая self, у метода нет параметров
        return: None
        """
        self.wait.until(EC.element_to_be_clickable(self.BASKET)).click()

    def add_products(self) -> None:
        """Последовательное добавление товара в корзину и переход в нее
        return: None
        """
        self.add_backpack()
        self.add_tshirt()
        self.add_sause_labs()
        self.click_basket()
