from playwright.sync_api import sync_playwright

def test_captcha_should_be_shown():
    with sync_playwright() as p:
        # Запускаем браузер
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Открываем Google
        page.goto("https://www.google.com/")

        # Нажимаем кнопку поиска
        search_input = page.locator("[name='q']")
        search_input.fill ("Javarush.ru")
        search_input.press("Enter")

        # Проверяем наличие текста на странице
        assert "About this page"in page.content()

        # Закрываем браузер
        browser.close()


