import time
from selenium.common.exceptions import (
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWebDriver:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self, url):
        self.browser.get(url)

    def find_class(self, class_name):
        return self.browser.find_element(By.CLASS_NAME, class_name)
    
    def find_tag(self, tag_name):
        return self.browser.find_element(By.TAG_NAME, tag_name)

    def find_xpath(self, xpath):
        return self.browser.find_element(By.XPATH, xpath)

    def find_id(self, id_name):
        return self.browser.find_element(By.ID, id_name)

    def wait_load(self, xpath, timeout):
        WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_load_clickable(self, xpath, timeout):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        
    def get_coocky(self):
        return self.browser.get_cookies()
        
    def implicitly_wait(self, time):
        self.browser.implicitly_wait(time)

    def refresh(self):
        self.browser.refresh()

    def quit(self):
        self.browser.close()
        self.browser.quit()
