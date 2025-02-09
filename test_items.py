from selenium.common.exceptions import NoSuchElementException


def test_check_enable_basket_button_on_catalogue_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    try:
        browser.find_element_by_class_name('btn-add-to-basket')
    except NoSuchElementException:
        assert 0, f"Элемент кнопки с классом \"btn-add-to-basket\" не найден на странице: {url}"



