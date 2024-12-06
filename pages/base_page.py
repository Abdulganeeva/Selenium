from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент с локатором {locator}",
        )

    def open(self, url):
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(("tag name", "body")),
            message="Страница не загрузилась",
        )
