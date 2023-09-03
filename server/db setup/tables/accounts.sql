CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    confirmation INTEGER DEFAULT 0,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    emails TEXT[],
    phone TEXT UNIQUE,
    created TIMESTAMP NOT NULL,
    deleted TIMESTAMP
)

CREATE TABLE changes (
    account_id INTEGER PRIMARY KEY,
    nickname TIMESTAMP[],
    password TIMESTAMP[],
    avatar TIMESTAMP[],
    FOREIGN KEY (account_id) REFERENCES accounts (id)
)

CREATE TABLE profiles (
    account_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    nickname TEXT,
    fast_avatar BYTEA,
    FOREIGN KEY (account_id) REFERENCES accounts (id),
    FOREIGN KEY (username) REFERENCES accounts (username)
)