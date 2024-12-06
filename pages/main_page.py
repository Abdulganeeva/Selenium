from .base_page import BasePage

# Локатор для текста в футере
text_locator = ('xpath', '//*[@id="__next"]/footer/div[5]/div/div/div[1]/p')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_text(self):
        return self.find(text_locator)
