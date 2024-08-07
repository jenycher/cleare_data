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
url = "https://tomsk.hh.ru/vacancies/programmist"


# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)


# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')
#vacancies = driver.find_elements(By.CLASS_NAME,'vacancy-card-container--OwxCdOj5QlSlCBZvSggS')

# Выводим вакансии на экран
#print(vacancies)
print(f"Найдено {len(vacancies)} вакансий")

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
   try:
   # Находим элементы внутри вакансий по значению
   # Находим названия вакансии
     title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
     # Находим названия компаний
     company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
      # Находим зарплаты
     salary = vacancy.find_element(By.CSS_SELECTOR, 'span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni').text
      # Находим ссылку с помощью атрибута 'href'
     link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   except:
     #print("произошла ошибка при парсинге")
     print(f"Произошла ошибка при парсинге: {e}")
     continue


   # Вносим найденную информацию в список
   parsed_data.append([title, company, salary, link])

# Закрываем подключение браузер
driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
     writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в hh.csv")