# animalTests

python -m pip -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

▎Использование API

Теперь вы можете использовать ваш API для выполнения следующих операций:

• GET /animal-tests/ — получить список всех тестов с агрегированной статистикой.

• GET /animal-tests/?animal_type=cow — получить список тестов для собак с агрегированной статистикой.

• POST /animal-tests/ — добавить новый тест с данными (animalname, testdate, productivity, healthstatus, animaltype).
