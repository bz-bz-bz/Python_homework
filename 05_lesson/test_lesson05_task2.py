from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    driver.find_element(By.NAME, "custname").send_keys("Мария")
    sleep(2)
    submit_btn = driver.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    driver.quit()
