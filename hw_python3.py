
from selene import browser, be, have


def test_google_1():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type ('Javarush.ru')
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))

def test_google_2():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type ('12312321321qqasfdas')
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('По запросу 12312321321qqasfdas ничего не найдено'))






