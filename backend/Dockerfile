FROM python:3.11-alpine

WORKDIR /app

# Установка uv
RUN pip install uv

COPY . .

RUN uv pip install --system -r requirements.txt

# Сборка статики
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
