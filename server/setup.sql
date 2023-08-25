CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    confirmation INTEGER,
    password TEXT,
    email TEXT UNIQUE,
    emails TEXT[],
    phone TEXT UNIQUE,
    nickname TEXT,
    profile TEXT,
    avatar BYTEA
)

CREATE TABLE changes (
    id INTEGER PRIMARY KEY,
    name TIMESTAMP[],
    nickname TIMESTAMP[],
    password TIMESTAMP[],
    avatar TIMESTAMP[],
    FOREIGN KEY (id) REFERENCES users (id)
)

CREATE TABLE tokens (
    id INTEGER NOT NULL,
    client TEXT NOT NULL,
    token TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES users (id)
)

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    title TEXT,
    users INTEGER[],
    roles INTEGER[],
    guild INTEGER,
    date TIMESTAMP
)

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    channel INTEGER UNIQUE,
    sender INTEGER,
    person INTEGER,
    t_data TEXT,
    b_data BYTEA,
    files TEXT[],
    date TIMESTAMP,
    FOREIGN KEY (channel) REFERENCES channels (id)
)
