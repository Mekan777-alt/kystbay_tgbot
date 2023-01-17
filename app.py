import logging
from config import dp, loop
from aiogram import executor
import heandlers


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup, loop=loop)
