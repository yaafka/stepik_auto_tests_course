from pages.product_page import ProductPage
from selenium import webdriver
import pytest
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(link):
    default_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    browser=webdriver.Chrome()
    productpage = ProductPage(browser, link)
    productpage.open(link)
    name_of_book_1 = productpage.find_xpath('//div[@class = "col-sm-6 product_main"]/h1').text
    sale_of_book_1 = productpage.find_xpath('//div[@class = "col-sm-6 product_main"]/p[@class = "price_color"]').text
    productpage.click_add_button()
    productpage.solve_quiz_and_get_code()
    name_of_book_2 = productpage.find_xpath('//div[@class = "col-sm-6 product_main"]/h1').text
    sale_of_book_2 = productpage.find_xpath('//div[@class = "alertinner "]/p/strong').text
    assert name_of_book_1 == name_of_book_2 and sale_of_book_1 == sale_of_book_2
    productpage.quit()