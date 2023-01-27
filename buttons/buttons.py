from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def nmts_cb():
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton('1', callback_data='1'))
    markup.add(InlineKeyboardButton('2', callback_data='2'))
    markup.add(InlineKeyboardButton('3', callback_data='3'))
    return markup
