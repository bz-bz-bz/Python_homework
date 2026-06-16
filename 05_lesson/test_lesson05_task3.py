from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_element():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10/0")
    driver.maximize_window()
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9
    for link in links:
        assert link.is_displayed()
    assert "1" in links[0].text
    driver.quit()
