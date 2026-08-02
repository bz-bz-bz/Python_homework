from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Auth_Page:
    """Класс для взаимодействия со страницей авторизации"""

    def __init__(self, driver) -> None:
        """Инициализация драйвера и поиск элементов на странице по ID
        return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.USERNAME = (By.ID, "user-name")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    def open_page(self) -> None:
        """Открытие страницы
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def username(self, username: str) -> None:
        """Поиск элемента на странице и ввод имени пользователя.
        username (str): Имя пользователя для ввода в форму,
        принимает только строчное значение
        return: None
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def password(self, password: str) -> None:
        """Поиск элемента на странице и ввод пароля.
        password (str): Пароль для ввода в форму,
        принимает только строчное значение
        return: None
        """
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def login_bttn(self) -> None:
        """Ожидание кликабельности элемента,
        после того, как элемент становится кликабельным,
        осуществляется клик на него
        Исключая self, у метода нет параметров
        return: None
        """
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username: str, password: str) -> None:
        """Последовательное заполнение формы и ее отправка
        username (str): Имя пользователя.
        password (str): Пароль пользователя.
        Все параметры принимают строчное значение
        return: None
        """
        self.username(username)
        self.password(password)
        self.login_bttn()
