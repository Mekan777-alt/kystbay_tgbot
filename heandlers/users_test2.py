from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from context.context import UsersTest_1
from buttons.buttons import nmts_cb


@dp.message_handler(text='Начать второе упражнение')
async def continue_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Туган')
    await message.answer("Давай рассмотрим еще составы кыстыбышек в наборе 'Ланч'", reply_markup=markup)


@dp.message_handler(text='1. Туган')
async def tugan(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('2. Тамле')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/tugan.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='2. Тамле')
async def tamle(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('3. Абый')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/tamle.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='3. Абый')
async def aby(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('4. Гомбэ')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/aby.PNG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='4. Гомбэ')
async def gombe(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('5. Апа')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/gombe.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='5. Апа')
async def apa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('6. Ак барс')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/apa.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='6. Ак барс')
async def ak_bars(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать третье упражнение')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/photo_2023-04-10 13.37.27.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
