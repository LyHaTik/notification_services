async def get_message(conn):
    return await conn.fetchrow("SELECT * FROM messages WHERE is_sent = FALSE ORDER BY id LIMIT 1")


async def get_users(conn):
    return await conn.fetch("SELECT * FROM users")


async def instert_log(conn, user_id, message_id, channel, status, error):
    return await conn.execute("""
        INSERT INTO send_logs (user_id, message_id, channel, status, error)
        VALUES ($1, $2, $3, $4, $5)
        """, user_id, message_id, channel, status, error)


async def update_status_message(conn, message_id):
    return await conn.execute("UPDATE messages SET is_sent = TRUE WHERE id = $1", message_id)