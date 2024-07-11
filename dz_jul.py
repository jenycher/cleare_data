import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/podvesnye-svetilniki"

driver.get(url)
time.sleep(3)


vacancies = driver.find_elements(By.CLASS_NAME, 'LlPhw')
print(f"Найдено {len(vacancies)} светильников")
parsed_data = []



for vacancy in vacancies:
    try:
        name = vacancy.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = vacancy.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        link = vacancy.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)