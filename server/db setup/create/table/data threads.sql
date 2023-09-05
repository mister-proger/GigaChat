CREATE TABLE public.channels (
    id BIGSERIAL,
    title TEXT,
    description TEXT,
    fast_avatar BYTEA,
    meta JSONB,
    created TIMESTAMP NOT NULL DEFAULT now(),
    deleted TIMESTAMP,
    PRIMARY KEY (id, title)
)

CREATE TABLE public.feeds (
    id BIGSERIAL,
    title TEXT,
    status TEXT,
    description TEXT,
    fast_avatar BYTEA,
    meta JSONB,
    chats BIGINT[]
)