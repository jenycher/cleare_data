import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/category/divany-i-kresla"

# Открываем веб-страницу
driver.get(url)

# Задаем 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с диванами с помощью названия класса
divans = driver.find_elements(By.CLASS_NAME, 'uKIho')

print(f"Найдено {len(divans)} диванов")

parsed_data = []

# Перебираем коллекцию диванов
for divan in divans:
    try:
        # Находим элементы внутри диванов по значению
        title = divan.find_element(By.CSS_SELECTOR, 'span.wYUX2').text
        print(title)
        parsed_data.append([title])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

# Закрываем подключение браузера
driver.quit()

# Записываем данные в CSV файл
with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название дивана'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в divans.csv")
