from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(x+y)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)

    sum = str(calc(x,y))

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(sum)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
