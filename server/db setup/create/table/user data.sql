CREATE TABLE public.accounts (
    id BIGSERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    confirmation INTEGER DEFAULT 0,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    emails TEXT[],
    phone TEXT UNIQUE,
    created TIMESTAMP NOT NULL,
    deleted BOOLEAN DEFAULT FALSE
)

CREATE TABLE public.accounts_changes (
    id INTEGER PRIMARY KEY,
    nickname TIMESTAMP[],
    password TIMESTAMP[],
    avatar TIMESTAMP[],
    FOREIGN KEY (id) REFERENCES public.accounts (id)
)

CREATE TABLE public.profiles (
    id INTEGER NOT NULL,
    username TEXT NOT NULL,
    nickname TEXT,
    fast_avatar BYTEA,
    FOREIGN KEY (id) REFERENCES public.accounts (id),
    FOREIGN KEY (username) REFERENCES public.accounts (username)
)

CREATE TABLE public.tokens (
    client BIGINT NOT NULL,
    agent TEXT NOT NULL,
    token TEXT NOT NULL,
    last_login TIMESTAMP,
    start TIMESTAMP NOT NULL,
    ending TIMESTAMP,
    FOREIGN KEY (client) REFERENCES public.accounts (id)
)

CREATE TABLE public.ttokens (
    client BIGINT NOT NULL,
    token TEXT NOT NULL,
    extradition TIMESTAMP NOT NULL,
    target TEXT NOT NULL,
    intentions TEXT NOT NULL,
    blocked TIMESTAMP,
    reason TEXT,
    comments TEXT[],
    FOREIGN KEY (client) REFERENCES public.accounts (id)
)