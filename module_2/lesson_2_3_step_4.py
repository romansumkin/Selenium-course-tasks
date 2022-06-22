from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

    alert = browser.switch_to_alert()
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)

    value = calc(x)

    answer= browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(value)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:

    time.sleep(20)
    browser.quit()