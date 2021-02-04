# Запуск backend
Для запуска потребуется файл ".env" в директории backend с необходимыми переменными окружения.

Пример содержимого файла:
```
SECRET_KEY=some_secret_key
DEBUG=0
ALLOWED_HOSTS=localhost 0.0.0.0 [::1]
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

Также потребуется установить нужные библиотеки из "requirements.txt". Например:
```console
$ python3 -m venv venv
$ source ./venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

Для первого запуска:
```console
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py runserver
```

# Запуск airtable_loader.py
Пример запуска:
```console
(venv) $ python3 airtable_loader.py -b <ваш_base_key> -a <ваш_api_key> -t <название_таблицы>
```

# Запуск frontend
```console
$ npm install
$ npm run dev
```

# Пример страницы
```
http://localhost:8080/therapists/<id>
```
