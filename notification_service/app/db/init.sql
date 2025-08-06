-- Таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    phone TEXT,
    telegram_id TEXT
);

-- Таблица сообщений
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    message TEXT,
    is_sent BOOLEAN DEFAULT FALSE
);

-- Логи отправки
CREATE TABLE send_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    message_id INTEGER REFERENCES messages(id),
    channel TEXT,
    status TEXT, -- 'success' или 'failure'
    error TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
