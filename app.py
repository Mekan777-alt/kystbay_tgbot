import logging
from config import dp, loop, db
from aiogram import executor
import heandlers


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False, loop=loop)
