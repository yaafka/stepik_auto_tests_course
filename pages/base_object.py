import time
from selenium.common.exceptions import (
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BaseWebDriver:
    def __init__(self,browser, url):
        self.browser = browser
        self.url = url

    def open(self, url):
        self.browser.get(url)
    
    def find_class(self, class_name):
        return self.browser.find_element(By.CLASS_NAME, class_name)
    
    def find_xpath(self, class_name):
        return self.browser.find_element(By.XPATH, class_name)
    
    def quit(self):
        self.browser.close()
        self.browser.quit()
