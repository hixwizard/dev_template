###### Название проекта

Монорепозиторий с Frontend (React) и Backend (Django) частями.

###### Структура

- `frontend/` - клиентская часть приложения (React)
- `backend/` - серверная часть приложения (Django)
- `shared/` - общие файлы и типы данных
- `infra/` - инфраструктура и конфигурация Docker

###### Запуск

Все команды Docker выполняются из директории `infra/`.
Переменные окружения берутся из файла `.env` в директории `infra/`.
`.env` хранить в `infra/` локально.

###### Подготовка окружения

1. Перейдите в директорию инфраструктуры:
```bash
cd infra
```

2. Скопируйте файл с примером переменных окружения и настройте его:
```bash
cp .env.example .env
```

3. Отредактируйте файл `.env` при необходимости:
```bash
nano .env  # или используйте любой текстовый редактор
```

###### Запуск полного стека (Frontend, Backend, Nginx, PostgreSQL)

Из директории `infra/` выполните:
```bash
docker-compose up --build
```

Для запуска в фоновом режиме:
```bash
docker-compose up -d --build
```

###### Запуск только базы данных для разработки

Если вы хотите работать с локальным Django-приложением, но использовать контейнеризованную базу данных:

1. Убедитесь, что вы находитесь в директории `infra/`:
```bash
cd infra
```

2. Запустите только базу данных:
```bash
docker-compose -f docker-compose.db.yaml up -d
```

3. Проверьте статус контейнера:
```bash
docker-compose -f docker-compose.db.yaml ps
```

4. Настройте Django для подключения к базе данных:
   - Убедитесь, что в `backend/config/settings.py` используются переменные окружения из `.env`
   - Выполните миграции:
```bash
cd ../backend
python manage.py migrate
```

5. Остановка базы данных:
```bash
cd ../infra
docker-compose -f docker-compose.db.yaml down
```

> Примечание: Для работы с базой данных убедитесь, что порт 5432 свободен.

###### Остановка всех сервисов

Из директории `infra/`:
```bash
docker-compose down
```

###### Просмотр логов

Для просмотра логов всех сервисов:
```bash
docker-compose logs -f
```

Для конкретного сервиса:
```bash
docker-compose logs -f frontend
docker-compose logs -f backend
docker-compose logs -f db
docker-compose logs -f nginx
```

###### Локальная разработка без Docker

###### Frontend
```bash
cd frontend
npm install
npm start
```

###### Backend
```bash
cd backend
# Установка зависимостей через uv
> Справка: https://habr.com/ru/articles/875840
```
```bash
pip install uv
uv pip install -r requirements.txt
# Или если uv уже установлен:
# uv pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
