CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    owner INTEGER NOT NULL,
    users INTEGER[],
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    created TIMESTAMP NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (owner) REFERENCES accounts (id)
)

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    channel INTEGER NOT NULL,
    author INTEGER NOT NULL,
    type CHAR(3) NOT NULL,
    text_content TEXT,
    bytea_content BYTEA,
    pinned BOOLEAN DEFAULT FALSE,
    attachments INTEGER[],
    shipped TIMESTAMP NOT NULL,
    forwarded INTEGER,
    FOREIGN KEY (channel) REFERENCES channels (id),
    FOREIGN KEY (author) REFERENCES accounts (id)
)

CREATE TABLE feeds (
    id SERIAL PRIMARY KEY,
    owner INTEGER NOT NULL,
    participants INTEGER[],
    FOREIGN KEY (owner) REFERENCES accounts (id)
)

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    feed INTEGER NOT NULL,
    author INTEGER NOT NULL,
    confirmator INTEGER NOT NULL,
    title TEXT,
    content TEXT,
    pinned BOOLEAN DEFAULT FALSE,
    header INTEGER[],
    footer INTEGER[],
    created TIMESTAMP NOT NULL,
    published INTEGER NOT NULL,
    FOREIGN KEY (feed) REFERENCES feeds (id),
    FOREIGN KEY (author) REFERENCES accounts (id),
    FOREIGN KEY (confirmator) REFERENCES accounts (id)
)