# test_login_and_save_cookies.py

from selenium import webdriver
import json
import time
import pytest


@pytest.mark.skip("It is intended to be run only once")
def test_login_and_save_data():
    SITE_URL = "https://ads.vk.com/"
    TIME_TO_LOGIN = 120

    driver = webdriver.Chrome()
    driver.get(SITE_URL)

    print(
        "Войдите в аккаунт вручную. localStorage и куки будут сохранены. У вас есть: {} секунд. Время пошло.".format(
            TIME_TO_LOGIN
        )
    )
    time.sleep(TIME_TO_LOGIN)  # время на ручной вход

    # --- Сохраняем куки ---
    cookies = driver.get_cookies()
    for cookie in cookies:
        cookie.pop("sameSite", None)
        cookie.pop("expiry", None)

    # --- Сохраняем localStorage ---
    local_storage = driver.execute_script("return window.localStorage;")

    # Сохраняем всё в JSON
    with open("session_data.json", "w") as f:
        json.dump({"cookies": cookies, "localStorage": local_storage}, f)

    driver.quit()
