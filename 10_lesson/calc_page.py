from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator_page:
    """Класс для взаимодействия со страницей калькулятора"""

    def __init__(self, driver) -> None:
        """Инициализация драйвера и поиск элементов на странице
        return: None
        """
        self.driver = driver
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.SCREEN_RESULT = (By.CSS_SELECTOR, ".screen")
        self.BTN_7 = (By.XPATH, "//span[text()='7']")
        self.BTN_PLUS = (By.XPATH, "//span[text()='+']")
        self.BTN_8 = (By.XPATH, "//span[text()='8']")
        self.BTN_EQUAL = (By.XPATH, "//span[text()='=']")

    def open_page(self) -> None:
        """Открытие страницы
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def enter_delay_value(self, seconds: str) -> None:
        """Осуществление поиска элемента на странице
        Очистка поля ввода, ввод нового значения
        seconds (str): колличество секунд для ввода в форму,
        принимает только строчное значение
        return: None
        """
        input_field = self.driver.find_element(*self.DELAY_INPUT)
        input_field.clear()
        input_field.send_keys(seconds)

    def click_seven(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.BTN_7).click()

    def click_plus(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.BTN_PLUS).click()

    def click_eight(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.BTN_8).click()

    def click_equal(self) -> None:
        """Осуществление поиска элемента на странице и клик по нему.
        Исключая self, у метода нет параметров
        return: None
        """
        self.driver.find_element(*self.BTN_EQUAL).click()

    def wait_for_result_text(self, expected_text: str) -> None:
        """Ожидание появления текста в элементе.
        return: None."""
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.SCREEN_RESULT, expected_text)
        )
