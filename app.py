import logging
from config import dp, loop, db_link
from aiogram import executor
import heandlers
import sqlite3


def create_table():
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT,
            name TEXT, 
            cafe TEXT);
        """
    )
    conn.commit()
    conn.close()


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    create_table()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False, loop=loop)
