import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура создания, настройки и закрытия веб-драйвера Chrome"""
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
