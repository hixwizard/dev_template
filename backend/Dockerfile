FROM python:3.11-slim

WORKDIR /app

# Установка uv
RUN pip install uv

# Копирование requirements и установка зависимостей
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Копирование остальных файлов
COPY . .

# Сборка статики
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
