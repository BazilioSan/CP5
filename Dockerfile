# Используем официальный образ Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для сборки расширений Python (например, psycopg2)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:${PATH}"

# Копируем файлы зависимостей в контейнер
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости Python через Poetry
RUN poetry install --no-root

# Копируем исходный код проекта в контейнер
COPY . .

# Команда по умолчанию для запуска приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]