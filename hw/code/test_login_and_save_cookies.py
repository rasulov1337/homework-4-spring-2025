# test_login_and_save_cookies.py

from selenium import webdriver
import json
import time

def test_login_and_save_data():
    driver = webdriver.Chrome()
    driver.get("https://ads.vk.com/")

    time_to_login = 120

    print("Войдите в аккаунт вручную. localStorage и куки будут сохранены. У вас есть: {} секунд. Время пошло.".format(time_to_login))
    time.sleep(time_to_login)  # время на ручной вход

    # --- Сохраняем куки ---
    cookies = driver.get_cookies()
    for cookie in cookies:
        cookie.pop('sameSite', None)
        cookie.pop('expiry', None)

    # --- Сохраняем localStorage ---
    local_storage = driver.execute_script("return window.localStorage;")
    
    # Сохраняем всё в JSON
    with open("session_data.json", "w") as f:
        json.dump({
            "cookies": cookies,
            "localStorage": local_storage
        }, f)

    driver.quit()