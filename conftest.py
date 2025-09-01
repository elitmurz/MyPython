import pytest

from selene import browser


@pytest.fixture(scope="function")
def browser_screen_size():
    browser.config.window_width = 1280
    browser.config.window_height = 840

    yield
    browser.quit()

    @pytest.fixture()
    def open_browser(browser_screen_size):
        browser_screen_size.open('https://www.google.com/')

    yield
    browser.quit()
