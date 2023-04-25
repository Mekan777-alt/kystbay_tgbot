from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ChatActions
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
    video = 'BAACAgIAAxkBAAIRS2RDGL_ZfWjk7ub7RybNIevbiBQVAAJbLQACXmgZSn1bK1Pj2VUlLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='2. Тамле')
async def tamle(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('3. Абый')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/tamle.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRTGRDGYsb6EQFMBBdZ1x_9pqbcyk_AAJdLQACXmgZSn3dvoSEBbyVLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='3. Абый')
async def aby(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('4. Гомбэ')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/aby.PNG', 'rb')
    video = 'BAACAgIAAxkBAAIRTWRDGixGV1QSjYXrVDg9byWD9jf5AAJeLQACXmgZShb-5Qr6fBCCLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='4. Гомбэ')
async def gombe(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('5. Апа')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/gombe.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRTmRDGpFwdCC4ov05MvYFvbIBzHRxAAJfLQACXmgZSvSiUaV_3cdzLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='5. Апа')
async def apa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('6. Ак барс')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/apa.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRT2RDGyNwGDeVo4IVFEaJbS_4K1NFAAJgLQACXmgZSlWxx704NSOTLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='6. Ак барс')
async def ak_bars(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('7. Кыстыбый Бэлэкэч')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/photo_2023-04-10 13.37.27.jpeg', 'rb')
    video = 'BAACAgIAAxkBAAIRUGRDG3nI847qHVPiEODa_NImTTqLAAJhLQACXmgZSkDg7B6kOqyLLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='7. Кыстыбый Бэлэкэч')
async def ak_bars(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('8. Кыстыбый с кашей')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/photo_2023-04-24 20.59.45.jpeg', 'rb')
    video = 'BAACAgIAAxkBAAIXCmRGwsTgGfKXeSZd2YbjwN3dmfLCAAJsKgACcUg4SocL6d6Ufe8oLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='8. Кыстыбый с кашей')
async def ak_bars(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать третье упражнение')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/photo_2023-04-24 20.57.04.jpeg', 'rb')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6914.MOV', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)