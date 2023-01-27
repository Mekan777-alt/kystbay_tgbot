import logging
from config import dp, loop
import heandlers
from aiogram import executor


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False, loop=loop)
