from pages.base_object import BaseWebDriver
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class AuthPage(BaseWebDriver):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_answer(self):
        return str(math.log(int(time.time())))

    def auth(self):
        self.browser.get(self.url)
