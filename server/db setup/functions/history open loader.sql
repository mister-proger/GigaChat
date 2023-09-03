CREATE FUNCTION get_message (user_id INTEGER, message_id INTEGER)
RETURNS SETOF messages
LANGUAGE plpgsql
AS
$$
BEGIN
    IF (
        EXISTS (
            SELECT 1
            FROM channels c
            JOIN messages m ON c.id = m.channel
            WHERE m.id = message_id AND user_id = ANY(c.users)
        )
        OR
        EXISTS (
            SELECT 1
            FROM channels c
            JOIN messages m ON c.id = m.channel
            WHERE m.id = message_id AND user_id = c.owner
        )
    ) THEN
        RETURN QUERY SELECT *
        FROM messages
        WHERE id = message_id;
    ELSE
        RETURN;
    END IF;
END;
$$;