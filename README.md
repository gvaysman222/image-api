# Image Gallery App

Простое приложение на Django REST Framework + Vue.js для загрузки, отображения и удаления картинок с описаниями. Все изображения хранятся непосредственно в базе данных в виде бинарных данных (Base64).

## Описание

- **Backend (Django + DRF)**  
  — реализует API с тремя эндпоинтами:  
  1. **POST** `/api/images/` — принимает JSON с полями  
     - `image` — строка data-URI (например, `"data:image/png;base64,AAA…"`),  
     - `description` — текстовое описание;  
     сохраняет картинку и описание в базе;  
  2. **GET** `/api/images/` — возвращает список записей `{ id, image, description, created_at }`, где `image` уже готовый data-URI;  
  3. **DELETE** `/api/images/{id}/` — удаляет запись по её ID.

- **Frontend (Vue 3 + Vite + Axios)**  
  — интерфейс:  
  - форма для выбора файла и ввода описания, конвертация файла в Base64 и отправка на бэкенд;  
  - галерея: выводит полученные из API data-URI в `<img>`, показывает описание и кнопку удаления.

## Технологии

- Python 3.9+  
- Django 4.x  
- Django REST Framework  
- Vue 3, Vite  
- Axios  
- SQLite (по умолчанию) или любая другая SQL-БД
- **python-dotenv** для управления переменными окружения


## Установка и запуск

### Backend

1. Создайте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
3. В корне backend/ создайте файл .env со следующим содержимым:
   ```bash
   DJANGO_SECRET_KEY=<ваш-секретный-ключ>
   DEBUG=True #или False если продакшн

4. Выполните миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Запустите сервер:
    ```bash
   python manage.py runserver

**API будет доступно на http://localhost:8000/api/images/.**

### Frontend
1. Перейдите в папку frontend/ и установите зависимости:
   ```bash
    cd frontend
    npm install
    npm install axios

2. Запустите Vite:
   ```bash
   npm run dev

**Приложение откроется в браузере по адресу http://localhost:3000.**