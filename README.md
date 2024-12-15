# AnimalTest API

## Описание

AnimalTest API — это RESTful API, разработанный с использованием Django Rest Framework для управления данными о тестах животных. API предоставляет возможность фильтрации и получения статистики по тестам.

## Установка

Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:

   git clone https://github.com/H8doubt/animalTests
   
2. Установите необходимые зависимости:

   pip install -r requirements.txt
   
3. Выполните миграции базы данных:

   python manage.py migrate
   
4. Запустите сервер разработки:

   python manage.py runserver

▎Использование API

Теперь вы можете использовать ваш API для выполнения следующих операций:

• GET /animal-tests/ — получить список всех тестов с агрегированной статистикой.

• GET /animal-tests/?animal_type=cow — получить список тестов для собак с агрегированной статистикой.

• POST /animal-tests/ — добавить новый тест с данными (animalname, testdate, productivity, healthstatus, animaltype).
