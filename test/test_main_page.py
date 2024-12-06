import allure


@allure.title("Тест на проверку текста в футере сайта Ситимобил")
def test_main_page(browser, main_page):
    expected_text = "Ситимобил — информационный сервис заказа транспортных и иных услуг, оказываемых партнерами. 0+"

    with allure.step("Открыть сайт Ситимобил"):
        main_page.open('https://city-mobil.ru/')

    with allure.step("Найти текст в футере"):
        text_object = main_page.find_text()

    with allure.step("Проверить, что текст соответствует ожидаемому"):
        assert text_object.text == expected_text, "Текст в футере сайта не соответствует ожидаемому"
