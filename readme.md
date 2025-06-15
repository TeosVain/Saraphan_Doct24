# Saraphan

Веб-приложение на Django для управления пользователями и товарами с использованием REST API.

## Описание

Проект реализует backend на Django с поддержкой авторизации, управления пользователями и товарами, а также предоставляет API с помощью Django REST Framework. Используются сторонние библиотеки для аутентификации, фильтрации и автогенерации документации.

## Основные технологии

- Python 3.12+
- Django 5.x
- Django REST Framework
- Djoser (аутентификация)
- django-filter (фильтрация)
- drf-yasg (Swagger/OpenAPI документация)
- SQLite (по умолчанию)

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone <URL-репозитория>
   cd Saraphan_Doct24
   ```

2. Создайте и активируйте виртуальное окружение:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

4. Примените миграции:
   ```sh
   cd saraphan
   python manage.py migrate
   ```

5. Создайте суперпользователя (по желанию):
   ```sh
   python manage.py createsuperuser
   ```

6. Запустите сервер:
   ```sh
   python manage.py runserver
   ```

## Структура проекта

- `saraphan/` — основной Django-проект
  - `api/` — приложение с API
  - `goods/` — приложение для управления товарами
  - `users/` — приложение для управления пользователями
- `media/` — директория для загружаемых файлов
- `db.sqlite3` — база данных (по умолчанию SQLite)
- `requirements.txt` — список зависимостей

## Документация API

После запуска сервера документация доступна по адресу:  
`http://localhost:8000/swagger/` (drf-yasg)

## Переменные окружения

- `SECRET_KEY` — секретный ключ Django (по умолчанию прописан в [saraphan/saraphan/settings.py](saraphan/saraphan/settings.py))
- `DEBUG` — режим отладки (True/False)
- `ALLOWED_HOSTS` — список разрешённых хостов

---

## Автор

TeosVain - Тимофей Кононов