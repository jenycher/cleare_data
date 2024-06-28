
#Разрабатываем программу с учётом всего того, что мы изучили.
#Мы будем парсить данные с сайта https://tomsk.hh.ru/vacancies/programmist и сохранять их в csv-файл.

# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
#driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/category/divany-i-kresla"


# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)


# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
divans = driver.find_elements(By.CLASS_NAME, 'uKIho')


# Выводим вакансии на экран
#print(vacancies)
print(f"Найдено {len(divans)} диванов")

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for divan in divans:
   try:
   # Находим элементы внутри диванов по значению
   # Находим названия дивана
     title = divan.find_element(By.CSS_NAME, 'span.wYUX2').text
     print(title)
     # Находим названия компаний
     #company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
      # Находим зарплаты
     #salary = vacancy.find_element(By.CSS_SELECTOR, 'span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni').text
      # Находим ссылку с помощью атрибута 'href'
     #link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   except:
     #print("произошла ошибка при парсинге")
     print(f"Произошла ошибка при парсинге: {e}")
     continue


   # Вносим найденную информацию в список
   parsed_data.append([title])

# Закрываем подключение браузер
driver.quit()
