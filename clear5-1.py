
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