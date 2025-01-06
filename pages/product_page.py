from pages.base_object import BaseWebDriver
from selenium.common.exceptions import NoAlertPresentException
import math


url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
button_add_selector = 'btn-add-to-basket'



class ProductPage(BaseWebDriver):
    def __init__(self,browser, url):
        super().__init__(browser, url)

    def click_add_button(self):
        self.find_class(button_add_selector).click()

    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")