CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    confirmation INTEGER DEFAULT 1,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    emails TEXT[],
    phone TEXT UNIQUE
)

CREATE TABLE changes (
    account_id INTEGER PRIMARY KEY,
    nickname TIMESTAMP[],
    password TIMESTAMP[],
    avatar TIMESTAMP[],
    FOREIGN KEY (account_id) REFERENCES accounts (id)
)

CREATE TABLE tokens (
    account_id INTEGER NOT NULL,
    agent TEXT NOT NULL,
    token TEXT NOT NULL,
    last_login TIMESTAMP,
    start TIMESTAMP NOT NULL,
    ending TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts (id)
)

CREATE TABLE ttokens (
    account_id INTEGER NOT NULL,
    token TEXT NOT NULL,
    extradition TIMESTAMP NOT NULL,
    target TEXT NOT NULL,
    intentions TEXT NOT NULL,
    comments TEXT[],
    FOREIGN KEY (account_id) REFERENCES accounts (id)
)

CREATE TABLE profiles (
    account_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    nickname TEXT DEFAULT name,
    fast_avatar BYTEA,
    FOREIGN KEY (account_id) REFERENCES accounts (id),
    FOREIGN KEY (username) REFERENCES accounts (username)
)

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    owner INTEGER NOT NULL,
    users INTEGER[],
    rights INTEGER[][],
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    created TIMESTAMP NOT NULL,
    pinned INTEGER[],
    FOREIGN KEY (owner) REFERENCES accounts (id)
)

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    channel INTEGER NOT NULL,
    author INTEGER NOT NULL,
    type CHAR(1) NOT NULL,
    text_content TEXT,
    bytea_content BYTEA,
    attachments INTEGER[],
    shipped TIMESTAMP NOT NULL,
    forwarded INTEGER,
    FOREIGN KEY (channel) REFERENCES channels (id),
    FOREIGN KEY (author) REFERENCES accounts (id)
)