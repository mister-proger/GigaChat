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
    blocked TIMESTAMP,
    reason TEXT,
    comments TEXT[],
    FOREIGN KEY (account_id) REFERENCES accounts (id)
)