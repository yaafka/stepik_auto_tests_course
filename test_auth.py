from pages.auth_page import AuthPage
from selenium import webdriver
import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_auth(link):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 15)
    browser.delete_all_cookies()
    authpage = AuthPage(browser, link)
    authpage.open(link)
    authpage.implicitly_wait(15)
    authpage.find_id('ember471').click()
    authpage.wait_load('//input[@type = "email"]', 15)
    authpage.find_xpath(
        '//input[@type = "email"]').send_keys('test@gmail.com')
    authpage.find_xpath(
        '//input[@type = "password"]').send_keys('mypassword')
    button_auth = authpage.find_xpath('//button[@type = "submit"]')
    button_auth.click()
    time.sleep(2)
    answer_element = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    answer = authpage.get_answer()
    answer_element.send_keys(answer)
    submit_button = browser.find_element(
        By.XPATH, '//button[@class ="submit-submission"]')
    submit_button.click()
    attempt_result = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//p[@class = "smart-hints__hint"]')))
    assert attempt_result.text == 'Correct!'
