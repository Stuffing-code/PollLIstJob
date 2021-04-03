# PollLIstJob

# Для разворота в локальном виде, после клонирования репозитория, необходимо:

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


# Список всех доступных api можно посмотреть по адресу http://127.0.0.1:8000/api/swagger/

# API:

#login и получение токена

Body:
username:
password

http://127.0.0.1:8000/auth/token/login


#Просмотр всех опросов

Body:

Headers:
Authorization: Token Authorization

http://127.0.0.1:8000/api/poll/all/


#Просмотр всех активных опросов:

Body:

Headers:
Authorization: Token Authorization

http://127.0.0.1:8000/api/poll/all_active/


# Удалить или обновить опрос:

http://127.0.0.1:8000/api/poll/update/<int:poll_id>

poll_id: id poll

Body:

poll_name: name poll
date_end: data format YYYY-MM-DD HH:HH:HH
poll_description: descriptions

Headers:
Authorization: Token Authorization


# Создание опроса:

http://127.0.0.1:8000/api/poll/create/

Body:
poll_name: name poll
date_start: data format YYYY-MM-DD HH:HH:HH
date_end: data format YYYY-MM-DD HH:HH:HH
poll_description: descriptions

Headers:

Authorization: Token Authorization


# Создание вопроса для опроса:

http://127.0.0.1:8000/api/question/create/

Body:

poll_name = id poll
text_question: text question max length 200
type_question: TEXT or CHOICE or MULTIPLE

Headers:

Authorization: Token Authorization


# Удалить или обновить вопрос:

http://127.0.0.1:8000/api/question/update/<int:question_id>

question_id = id question

Body:
poll_name = id poll
text_question: text question max length 200
type_question: TEXT or CHOICE or MULTIPLE

Headers:
Authorization: Token Authorization


# Создать варианты ответов:

http://127.0.0.1:8000/api/choice/create/

Body:
question = id question
value = choice value

Headers:
Authorization: Token Authorization


# Обновить или удалить варианты ответов:

http://127.0.0.1:8000/api/choice/update/<int:choice_id>

choice_id: choice id

Body:

question = id question
value = choice value

Headers:
Authorization: Token Authorization


# Просмотр проведеного опроса для определенного пользователя:

http://127.0.0.1:8000/api/answer/view/<int:user_id>

user_id: user id
Body:


Headers:
Authorization: Token Authorization


# Обновить или удалить ответы:

http://127.0.0.1:8000/api/answer/update/<int:answer_id>

answer_id:  answer id

Body:
value: value

Headers:
Authorization: Token Authorization


# Создание ответов на опрос:

http://127.0.0.1:8000/api/answer/create/

Body:
user_voter:  voter id
value: value

Headers:
Authorization: Token Authorization


# Создание голосуещего:

http://127.0.0.1:8000/api/voter/create/

Body:
poll:  poll id
user: id register user

Headers:
Authorization: Token Authorization


# Прсмотр всех голосуещего и всех проходимых им опросов

http://127.0.0.1:8000/api/voter/<int:user_id>

user_id = id user voter

Body:

Headers:
Authorization: Token Authorization


# Удаление всех опросов для пользователя:

http://127.0.0.1:8000/api/voter/voter/<int:user_id>

user_id = id user voter

Body:

Headers:
Authorization: Token Authorization
