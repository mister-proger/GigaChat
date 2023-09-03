CREATE TABLE permissions (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)

CREATE TABLE channels_permissions (
    channel INTEGER NOT NULL,
    user_id INTEGER,
    permission INTEGER NOT NULL,
    status BOOLEAN,
    FOREIGN KEY (channel) REFERENCES channels (id),
    FOREIGN KEY (user_id) REFERENCES accounts (id),
    FOREIGN KEY (permission) REFERENCES permissions (id)
)

CREATE TABLE feeds_permissions (
    feed INTEGER PRIMARY KEY,
    user_id INTEGER,
    permission INTEGER NOT NULL,
    status BOOLEAN,
    FOREIGN KEY (feed) REFERENCES feeds (id),
    FOREIGN KEY (user_id) REFERENCES accounts (id),
    FOREIGN KEY (permission) REFERENCES permissions (id)
)