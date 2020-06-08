import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_button_shopping_cart(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_css_selector(".add-to-basket .btn")
    assert button, "Should be button with the addition of the product to cart"