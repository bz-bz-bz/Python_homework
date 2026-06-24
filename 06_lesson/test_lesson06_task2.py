from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    driver.maximize_window()
    driver.add_cookie({
      "name": "SESSION",
      "value": "Y2Q4ZGMyNDEtZjFjOC00ZWZhLWEyOWItZDRhYTRlNjQ1NmJm",
      "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/testtst")
    url_1 = driver.current_url
    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
      "name": "SESSION",
      "value": "N2NlYTM1YzAtMzM5Yi00NzcwLTk4NzctNTFjNzExMGFjMGJk",
      "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/testtttst")
    url_2 = driver.current_url
    assert (url_1 != url_2), "Ошибка, URl пользователей совпадают!"
    driver.quit()
