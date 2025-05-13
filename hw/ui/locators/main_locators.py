from selenium.webdriver.common.by import By


class MainPageLocators():
    SHOW_SEARCH_INPUT_BUTTON = (By.XPATH, r"//div[@aria-label='Открыть поиск']")
    SEARCH_INPUT = (By.XPATH, '//form/input')
    MORE_INFO_ABOUT_CURRENT_LESSON_BUTTON = (By.XPATH, '//aside//div/a[contains(@class, "title")]')
    DAY_OF_WEEK_BUTTON = lambda self, day_of_week: (By.XPATH, '//aside//span[contains(text(), "{}")]'.format(day_of_week))
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')
