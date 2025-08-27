from selene import browser, have

def test_captcha_should_be_shown():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type ('Javarush.ru')
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))


