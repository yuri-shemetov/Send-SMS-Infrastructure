## Задачи:
1. Разработать REST API для отправки СМС-уведомлений через каналы Viber/SMS.
2. Создать python-скрипт для примера, который формирует таблицу клиентов и тексты сообщений для рассылки.
3. Настроить процесс валидации и приема python-скрипта от другого подразделения Банка.
4. Реализовать запуск и остановку работы скрипта на протяжении одной недели с периодическим запуском каждый час.
5. Учесть временной период с 22:00 до 09:00, когда работа скрипта не должна выполняться.

## Запуск приложения
- Клонируем ссылку
```bash
git clone https://github.com/yuri-shemetov/Send-SMS-Infrastructure.git
```
- Приложение использует инструмент [poetry](https://python-poetry.org/) для управления зависимостями. Вам необходимо его установить, до начала работы
```bash
pip install --user poetry
poetry install
poetry --version
```
- Запустить Reddis из docker-compose:
```bash
sudo docker compose -f docker-compose.yml up --build
```

- Переходим в папку SRC: `cd src`. Вам необходимо будет настроить вашу копию .env для работы с приложением. Хорошим стартом будет копирование файла .`env.dist в .env.`

- Запускаем миграции
```bash
poetry run manage.py makemigrate
```
- При необходимости создаем суперюзера для админки
```bash
poetry run  manage.py createsuperuser
```
- Запускаем локальный сервер, а также Celery (worker - тот, кто выполняет задачу; beat - тот, кто следит за графиком)
```bash
poetry run ./manage.py runserver
poetry run celery -A project_settings worker -l INFO
poetry run celery -A project_settings beat -l INFO
```

## Общая информация по работе с API

Для работы с сервисом рекомендуется использовать Postman. Для начала Вам необходимо зарегистрироваться. Пример:
```bash
POST: api/users/registration/
{
    "username": "dummy",
    "email": "dummy@email.com",
    "password": "password"
}
```

В результате чего, Вы должны получить ответ. Пример:
```bash
{
    "username": "dummy",
    "email": "dummy@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNjkzNzM2OTAyfQ.2xQxMzwgPO3pDp53dLp2T3IKUfyteScQT7FlvRvUvFk"
}
```
Вы получаете токен доступа, который нужно предоставить всякий раз, когда необходимо создать базу клиентов, сообщения и рассылки.