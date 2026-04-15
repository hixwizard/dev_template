#### Название проекта

Монорепозиторий с Frontend (React) и Backend (Django) частями.

##### Структура проекта

- `frontend/` - клиентская часть приложения (React)
- `backend/` - серверная часть приложения (Django)
- `shared/` - общие файлы и типы данных

##### Запуск проекта

##### Frontend
```bash
cd frontend
npm install
npm start
```

##### Backend
```bash
cd backend
# Установка зависимостей через uv
# Справка: https://habr.com/ru/articles/875840/

pip install uv
uv pip install -r requirements.txt
# Или если uv уже установлен:
# uv pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

##### Docker
Для запуска всего приложения с помощью Docker:
```bash
docker-compose up --build
```

##### База данных для разработки
Для разработки можно запустить только базу данных в Docker, чтобы подключать к ней Django-приложение локально:

1. Скопируйте файл окружения:
```bash
cp .env.example .env
```

2. Запустите базу данных:
```bash
cd ..
docker-compose -f docker-compose.db.yaml up -d
```

3. Проверьте, что база данных работает:
```bash
docker-compose -f docker-compose.db.yaml ps
```

4. Настройте Django для подключения к базе данных:
   - Убедитесь, что в `backend/config/settings.py` используются переменные окружения из `.env`
   - Выполните миграции:
```bash
cd backend
python manage.py migrate
```

5. Остановка базы данных:
```bash
docker-compose -f docker-compose.db.yaml down
```

> Примечание: Для работы с базой данных убедитесь, что порт 5432 свободен.
