from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# link = "http://suninjuly.github.io/registration1.html"
link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # first_name
    input1 = browser.find_element(By.XPATH, '//*[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    # last_name
    input2 = browser.find_element(By.XPATH, '//*[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    # email
    input3 = browser.find_element(By.XPATH, '//*[@placeholder="Input your email"]')
    input3.send_keys("example@example.ru")
    # phone
    input4 = browser.find_element(By.XPATH, '//*[@placeholder="Input your phone:"]')
    input4.send_keys("+79999999999")
    # adres
    input4 = browser.find_element(By.XPATH, '//*[@placeholder="Input your address:"]')
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
