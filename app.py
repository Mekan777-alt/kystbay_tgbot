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
            cafe TEXT, 
            test2_1 TEXT,
            at_1 TEXT,
            at_2 TEXT,
            at_3 TEXT,
            at_4 TEXT,
            at_5 TEXT,
            at_6 TEXT,
            at_7 TEXT,
            at_8 TEXT,
            at_9 TEXT,
            at_10 TEXT,
            at_11 TEXT,
            at_12 TEXT,
            at_13 TEXT,
            at_14 TEXT,
            at_15 TEXT,
            at_16 TEXT,
            at_17 TEXT,
            at_18 TEXT,
            at_19 TEXT);
        """
    )
    conn.commit()
    conn.close()


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    create_table()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False, loop=loop)
