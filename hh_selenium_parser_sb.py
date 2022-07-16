import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()  # Запускаем браузер Хром (он сразу закроется)
# chromedriver ТОЙ ЖЕ ВЕРСИИ ЧТО И ХРОМ
browser.maximize_window()  # На весь экран
browser.get("https://hh.ru/")  # Открываем ХХ

# Находим кнопку
search_button = browser.find_element(By.CSS_SELECTOR, '[data-page-analytics-event="searchButton.submit"]')

# Находим поле ввода
search_input = browser.find_element(By.ID, "a11y-search-input")  # Ищем элемент по ID
search_input.send_keys("Программист Python")  # Напечатать в поле

# Кликаем по кнопку
search_button.click()

# Находим текст зарплаты
salary_xpath = '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div[6]/div/div[2]/li[6]/label/span/span[1]'

# WebDriverWait - ждать вплоть до 20 сек
# Ждем presence_of_element_located - элемент появился на странице
# Какой элемент: (By, "")
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, salary_xpath)))

try:
    salary = browser.find_element(By.XPATH, salary_xpath)
except:
    print("NOT FOUND")
    time.sleep(10)
# # И кол-во вакансий
# count_xpath = '/html/body/div[5]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div[4]/div/div[2]/li[6]/label/span/span[2]/span'
# count = browser.find_element(By.XPATH, count_xpath)

# Отфильтровать только цифры
import re

salary_integer = re.sub(r"\D", "", salary.text)  # Умная замена в текста r"\D" = "Все символы кроме 0-9"

print(f"Max Salary = {salary_integer}")

time.sleep(5)  # 5 секунд спим
browser.close()  # Закрываем