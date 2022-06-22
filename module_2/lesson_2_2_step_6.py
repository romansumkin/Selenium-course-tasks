from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)

    value = str(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(value)

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
