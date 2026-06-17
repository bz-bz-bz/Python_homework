from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    sleep(5)
    driver.find_element(By.LINK_TEXT, "HTML form").click()
    sleep(7)
    assert "/forms/post" in driver.current_url, "Неверный url сайта!"
    driver.back()
    sleep(2)
    assert driver.current_url == "https://httpbin.org/", "URL сайта "
    "не совпадает c driver.current_url"
    driver.quit()
