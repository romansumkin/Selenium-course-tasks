from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("asd@asd.com")

    choose_file = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson_2_2_step_8_file.txt')
    choose_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
