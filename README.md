# API для Yatube

## Описание:

Yatube — это платформа для блогов. Все блоги чем-то похожи друг на друга: любой блог-сервис предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AnnZebel/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### _Документация:_ 

http://127.0.0.1:8000/redoc/
