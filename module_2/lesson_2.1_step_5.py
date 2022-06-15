from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    answer= browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotsRule")
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
