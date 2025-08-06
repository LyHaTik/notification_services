# Notification Service

Сервис для отправки уведомлений пользователям с использованием FastAPI и PostgreSQL, контейнеризированный через Docker и Docker Compose.

---

## Описание

Данный проект запускает REST API на FastAPI, который взаимодействует с базой данных PostgreSQL. Все сервисы запускаются в контейнерах Docker, настроенных в `docker-compose.yml`.

---

## Стек технологий

- Python 3.11 (FastAPI, asyncpg)
- PostgreSQL 15
- Docker & Docker Compose
- Uvicorn (ASGI сервер)

---

## Как запустить

### 1. Клонировать репозиторий

bash
git clone <URL_твоего_репозитория>
cd <папка_проекта>

### 2. Создать файл .env в корне проекта
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=notifier
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

API_TG_ID=your_api_id
API_TG_HASH=your_api_hash
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=you@example.com
SMTP_PASSWORD=your_password

### 3. Запустить сервисы
docker-compose up --build

---

## Доступ к сервису
API доступно по адресу: http://localhost:8000
Документация Swagger UI: http://localhost:8000/docs

---

## Структура проекта
.
│──notification_service/
│   ├── app/
│   │   ├── main.py                     # Точка входа FastAPI приложения
│   │   ├── models.py
│   │   ├── notification_service.py
│   │   ├── service.py                  # Логика обработки уведомлений
│   │   ├── db/
│   │   │   ├── func.py                 # Функции работы с БД
│   │   │   ├── connect.py              # Подключение к БД
│   │   │   └── init.sql                # SQL-скрипт инициализации БД
│   │   └── notifier/
│   │       ├── base.py                 # Базовый класс отправки
│   │       ├── email_notifier.py       # Отправка email
│   │       ├── sms_notifier.py         # Отправка sms
│   │       └── telegram_notifier.py    # Отправка в Telegram
│   ├── requirements.txt            # Python-зависимости
│   └── Dockerfile                  # Описание образа приложения
├── docker-compose.yml              # Описание сервисов Docker
├── .env                            # Файл с конфигурацией (не в репозитории)
└── README.md                       # Этот файл

---

## Советы и рекомендации
Внутри контейнеров сервисы общаются по имени сервиса из docker-compose.yml (db для PostgreSQL).
Порт PostgreSQL 5432 проброшен на 5400 на хост-машине для удобного локального доступа.

---

## Тестирование работы
Для тестирования приложения следует минимально заполнить БД, тиаблицу users и messages.
Статусы отправки сообщений записываются в таблицу send_logs