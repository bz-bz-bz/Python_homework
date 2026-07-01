from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.NAME, "first-name"))).send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR,
                        ".btn.btn-outline-primary.mt-3").click()
    zip_classes = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_classes
    form_name = ["first-name", "last-name", "address", "city", "country",
                 "e-mail", "phone,", "job-position", "company"]
    for field_id in form_name:
        driver.find_element(By.CSS_SELECTOR, f"#{field_id}.alert-success")
    driver.quit()
