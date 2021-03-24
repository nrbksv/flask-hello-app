# Наше первое приложение на [Flask](https://flask.palletsprojects.com/)

Для того, чтобы запустить данное приложение у вас должны быть установлены:
 - python >= 3.8
 - pip
 - vitualenv


## Запуск приложения
Находясь в директории проекта выполните следующие шаги для запуска приложения:

### Виртуальное окружение:
Создайте виртуальное окружение командой:
```bash
python3 -m virtualenv -p python3 venv
```

Активируйте виртуальное окружение командой:
```bash
source venv/bin/activate
```


### Установка зависимостей:
для установки зависимостей выполните команду
```bash
pip install -r requirements.txt
```

### Переменные окружения
Копируйте файл `.env.sample` с именем копии `.env`:
```shell
cp .env/sample .env
```

В фале `.env` замините значения переменных окружения на требуемые.

Переменные коружения:
 - `SECRET_KEY` - [Секретный ключ Flask-приложения](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY)
 - `FLASK_ENV` - Окружение приложения. Определяет какие параметры будут активированы применены (см. Файл `src/config`). Доступны варианты `production` и `development`


### Запуск приложения

Для запуска приложения выполните команду 
```bash
source run_server.sh
```


## Вклад в проект:
Для того, чтобы сделать вклад в проект нужно:
[Сделать форк репозитория](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo), внести изменения и [создать запрос на слияние](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)


Задачи, которые ждут, чтобы их выполнили за дополнительные баллы можно найти, кликнув на [эту ссылку](https://github.com/md5orsha256/flask-hello-app/issues?q=is%3Aopen+is%3Aissue)


* Задачи можно брать только те, которые ни на кого не назначены

* Над задачей может работать только один человек.

* Начав выполнение задачи разработчик должен назначить задачу на себя. Если этого не сделано - значит задача свободна и её может выполнять другой разработчик.

* Если хотите реализовать какую-то задачу и не можете взять её на себя - напишите об этом в комментарий к задаче или мне в телеграм

* Все коммиты должны содержать в сообщении номер задачу (например: `#23 Добавил форму для создания комментария`).

* Количество баллов, начисляемое за задачу указано в описании каждой задачи.
