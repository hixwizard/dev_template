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
