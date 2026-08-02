from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Information_Page:
    """Класс для взаимодействия со страницей ввода персональных данных"""

    def __init__(self, driver) -> None:
        """Инициализация драйвера и поиск элементов на странице по ID
        return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE = (By.ID, "continue")

    def firstname(self, firstname: str) -> None:
        """Осуществление поиска элемента на странице и ввод имени пользователя.
        firstname (str): Имя пользователя для ввода в форму,
        принимает только строчное значение
        return: None
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)

    def lastname(self, lastname: str) -> None:
        """
        Осуществление поиска элемента на странице и ввод фамилии пользователя.
        lastname (str): Имя пользователя для ввода в форму,
        принимает только строчное значение
        return: None
        """
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)

    def postal_code(self, postal_code: str) -> None:
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        """
        Осуществление поиска элемента на странице и ввод почтового индекса
        postal_code (str): Почтовый индекс для ввода в форму,
        принимает только строчное значение
        return: None
        """

    def continue_bttn(self) -> None:
        """
        Функция отвечает за ожидание кликабельности элемента,
        после того, как элемент становится кликабельным,
        осуществляется клик на него
        Исключая self, у метода нет параметров
        return: None
        """
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def full_info_form(
        self, firstname: str, lastname: str, postal_code: str
    ) -> None:
        """Последовательное заполнение формы и ее отправка
        firstname (str): Имя пользователя.
        lastname (str): Фамилия пользователя.
        postal_code (str): Почтовый индекс.
        Все параметры принимают строчное значение
        return: None
        """
        self.firstname(firstname)
        self.lastname(lastname)
        self.postal_code(postal_code)
        self.continue_bttn()
