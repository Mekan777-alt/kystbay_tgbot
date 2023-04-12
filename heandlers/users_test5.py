from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from buttons.buttons import nmts_cb
from context.context import UsersTest_1


@dp.message_handler(text='Я красавчик(ца), идем дальше.')
async def lesson3(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие заведения,снятие сигнализации,включение вытяжки, света в кафе.')
    await message.answer("Дорогой друг, мы с тобой приступаем к крайнему уроку, где полностью разберем зону кассы, "
                         "скрипты, оформление доставки, включение оборудования в зале и инструкции к ним. Разберем с "
                         "тобой чек листы, регламенты уборки, да и в целом расскажу тебе как будет выглядет твой "
                         "рабочий день. \n"
                         "\n"
                         "Не будем терять твое время, приступим.", reply_markup=markup)


@dp.message_handler(text='Открытие заведения,снятие сигнализации,включение вытяжки, света в кафе.')
async def open_smen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как открывать и закрывать рабочую смену')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            file = 'BQACAgIAAxkBAAICrGQ0MhaHB_O3dcVvhnKs6UkDiENiAAJ4MQACTCigSUc0DdutDdukLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=file, reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/obzholodpush.MP4', 'rb')
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            doc = 'BQACAgIAAxkBAAICqWQ0LVK5vUmXmuOKw8hR3cmdag3qAAIqMQACTCigSTlZFROorzUjLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            doc = 'BQACAgIAAxkBAAICqmQ0MTCDOLmFgyqvp1ltqQnE_cy8AAJhMQACTCigSZl61jZzUevTLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            doc = ''
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Как открывать и закрывать рабочую смену')
async def open_smen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие кассы и рабочей смены')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие кассы и рабочей смены')
async def open_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с кассой')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с кассой')
async def problem_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие киосков')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие киосков')
async def open_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с киосками')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с киосками')
async def problem_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Включение ТВ, экрана выдачи заказа')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Включение ТВ, экрана выдачи заказа')
async def vkl_vykl_tv(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент по уборке зала и туалетов')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Регламент по уборке зала и туалетов')
async def reglament_bathroom(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обязанности кассира')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Молодец! Теперь ты умеешь открывать заведение. Настало время применить знания на практике. "
                         "Проинформируй своего руководителя об этом и отправь фотоотчет ему по открытию кассы, "
                         "киосков, ТВ. Короче, красавчик, дерзай! ")


@dp.message_handler(text='Обязанности кассира')
async def obyaz_kass(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
async def dock_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Оформление доставки на кассе, чеки для  доставки, закрытие доставок')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Оформление доставки на кассе, чеки для  доставки, закрытие доставок')
async def ofor_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Скрипт кассира')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Скрипт кассира')
async def script_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
async def konflikt_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Дополнительные обязанности кассира')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Дополнительные обязанности кассира')
async def bonus_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Закрытие смены. Чек-лист закрытия')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Ярар, хеппи енд близок, а может и нет)))Хихихихииииии:D Все уже, заканчиваем. Почти))")
    await message.answer("Давай научимся закрывать смену. Администратор вечером сам закроет кассу, киоски и сделает "
                         "отчет по выручке дня, поэтому тебе нужно будет совместно с командой сдать чистую смену, "
                         "выключить оборудования, свет, поставить на сигнализацию кафе и заполнить чек-лист закрытия "
                         "по чистоте. Здесь тебе будет не сложно")


@dp.message_handler(text='Закрытие смены. Как закрывать кассу, киоск. Убрать помещение')
async def close_work(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист закрытия')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Чек-лист закрытия')
async def check_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист по бытовой химии')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Чек-лист по бытовой химии')
async def chek_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Приступить к АТТЕСТАЦИИ.')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("КРАССАВИЧИК!\n"
                         "А теперь давай пройдем еще и аттестацию :) добью тебя сегодня =)", reply_markup=markup)

