
**REST - service for receiving requests to enter the premises**
 -
 
  * Пользоатели: посетители и менеджеры. 
  * Посетитель создает заявку, менеджер подтверждает или отказывает.

\
**For start project**

1) python -m venv myvenv
2) myvenv\Scripts\activate
3) pip install -r requirements.pip
4) create webapp in postgreysql
5) in django:
  * python manage.py makemigrations webapp
  * python manage.py makemigrations 
  * python manage.py migrate
  * python manage.py createsuperuser --email admin@example.com --username admin
  * python manage.py runserver

\
**How it works**
1) перед регистрацией пользователей в админке приложения необходимо создать 2 группы ('managers' и 'clients') иначе запросы не пройдут
2) Для того чтобы пользователь мог редактировать или удалять (его через web админку нужно добавить в группу 'managers')
3) использовать curl

* для регистрации \
curl -X POST http://127.0.0.1:8000/rest/registration/ --data "username=roman&email=roman@example.com&password=r4r4r4r4"
получили токен 474dfb85a3f6cd208eb2ca0a43f44b795925a3f9

* для проверки аунтификации пользователя \
curl http://127.0.0.1:8000/rest/auth/ -H "Authorization: Token fe23e1d062ca212286de651b685ac3e6e4b2fda1"

* отправить запрос (только авторизованный пользователь) \
curl -H "Authorization: Token 474dfb85a3f6cd208eb2ca0a43f44b795925a3f9" -d "name=roman&space_name=office" "http://127.0.0.1:8000/rest/send_request/"

* все запросы (только менеджер) \
curl http://127.0.0.1:8000/rest/all_requests/ -H "Authorization: Token 72c6c875c016291fd3cba53d4d07cb3d839dbab3"

* статус заявки (только клиент) по id заявки и своему токену \
curl http://127.0.0.1:8000/rest/access/1/ -H "Authorization: Token 474dfb85a3f6cd208eb2ca0a43f44b795925a3f9"

* подтверждение или отказ заявки (только менеджером) токен менеджера \
curl -X PUT -H "Authorization: Token 72c6c875c016291fd3cba53d4d07cb3d839dbab3" -d "name=roman&space_name=office&access=no" "http://127.0.0.1:8000/rest/access/1/"   

* удалить запрос \
curl -X DELETE -H "Authorization: Token 72c6c875c016291fd3cba53d4d07cb3d839dbab3"  "http://127.0.0.1:8000/rest/access/1/"