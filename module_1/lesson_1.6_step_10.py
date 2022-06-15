from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input1.send_keys("Testov")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input2.send_keys("Petrov@rov.com")
    input3 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()