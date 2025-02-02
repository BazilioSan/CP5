# Проект курсовой работы №5 DRF

## Описание:

Веб приложение
Трекер привычек


## Функционал:
Реализация бэкенда по отслеживанию привычек пользователя, и напоминанием об их выполнении через телеграм бот

```bash
git clone https://github.com/BazilioSan/CP5.git
cd polevaya_cw_drf
```
 
2. Собрать и запустить контейнеры:
```bash
docker-compose up --build
```
 
3. Применить миграции:
```bash
docker-compose exec web python manage.py migrate
```
 
4. Создать суперпользователя:
```bash
docker-compose exec web python manage.py csu
```
 
5. Доступно по адресу: http://localhost:8000


## Локальная Установка:

1. Клонируйте репозиторий:
```
git clone github.com/BazilioSan/CP5
```
2. Установите зависимости:
```
pip install poetry
poetry install
poetry update

```
3. Установите параметры доступа
```
Особые параметры доступа отсутствуют
```
## Использование:

Уточняется

## Документация:

Для получения дополнительной информации запустите локальный сервер и обратитесь к [документации](http://127.0.0.1:8000/swagger/?format=openapi).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

