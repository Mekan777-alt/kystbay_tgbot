from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ChatActions
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
async def open_smen(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как открывать и закрывать рабочую смену')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            # file = 'BQACAgIAAxkBAAICrGQ0MhaHB_O3dcVvhnKs6UkDiENiAAJ4MQACTCigSUc0DdutDdukLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=file, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            # doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/obzholodpush.MP4', 'rb')
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            doc = 'BAACAgIAAxkBAAIFlGQ2v53Qy38L0xDAtPdVU34jNvDMAAJaKgACNCKwSfOwXOYS3btyLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            doc = 'BAACAgIAAxkBAAIFlWQ2wGh-TSGw2_wzIPsmjnhbCa-DAAJiKgACNCKwSb9ilm6KHdD7LwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            doc = 'BAACAgIAAxkBAAIFk2Q2v3QN6n5_BHnVvGsj7C7kgEuqAAJVKgACNCKwSXG6M9WOdspKLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Как открывать и закрывать рабочую смену')
async def open_smen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие кассы и рабочей смены')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие кассы и рабочей смены')
async def open_kassa(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с кассой')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            # file = 'BQACAgIAAxkBAAICrGQ0MhaHB_O3dcVvhnKs6UkDiENiAAJ4MQACTCigSUc0DdutDdukLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=file, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6117.MP4', 'rb')
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            doc = 'BAACAgIAAxkBAAIFlmQ2wxb1LiFMxrJ9LMGJ8cDu8OjrAAJ0KgACNCKwSRj4Ns4vHLhWLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            # doc = 'BAACAgIAAxkBAAIFlWQ2wGh-TSGw2_wzIPsmjnhbCa-DAAJiKgACNCKwSb9ilm6KHdD7LwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            # doc = 'BAACAgIAAxkBAAIFk2Q2v3QN6n5_BHnVvGsj7C7kgEuqAAJVKgACNCKwSXG6M9WOdspKLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с кассой')
async def problem_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие киосков')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие киосков')
async def open_kiosk(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с киосками')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6011.MP4', 'rb')
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=file, reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            # doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6117.MP4', 'rb')
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            doc = 'BAACAgIAAxkBAAIFmGQ2xFqpjJnW6RKg893lTkxJndgvAAKIKgACNCKwSQEtf5jXi3IVLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            doc = 'BAACAgIAAxkBAAIFl2Q2xDZ3xS60D7mgxRXXzcDEGaJZAAKEKgACNCKwSXxqt1knD9AKLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            # doc = 'BAACAgIAAxkBAAIFk2Q2v3QN6n5_BHnVvGsj7C7kgEuqAAJVKgACNCKwSXG6M9WOdspKLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)

@dp.message_handler(text='Проблемы в работе с киосками')
async def problem_kiosk(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Включение ТВ, экрана выдачи заказа')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            # file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6011.MP4', 'rb')
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=file, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            doc = 'BAACAgIAAxkBAAIFmWQ2xh-SgbsicEP7Ev921ahO8IKVAAKVKgACNCKwSRaPluEKh3NMLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            # doc = 'BAACAgIAAxkBAAIFmGQ2xFqpjJnW6RKg893lTkxJndgvAAKIKgACNCKwSQEtf5jXi3IVLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            # doc = 'BAACAgIAAxkBAAIFl2Q2xDZ3xS60D7mgxRXXzcDEGaJZAAKEKgACNCKwSXxqt1knD9AKLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            doc = 'BAACAgIAAxkBAAIFmmQ2xw6ECYW1r2zVIQ6VqH2gHsR0AALgLAACNCK4ST3JnbwdjIb4LwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Включение ТВ, экрана выдачи заказа')
async def vkl_vykl_tv(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент по уборке зала и туалетов')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            # file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6011.MP4', 'rb')
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=file, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            # doc = 'BAACAgIAAxkBAAIFmWQ2xh-SgbsicEP7Ev921ahO8IKVAAKVKgACNCKwSRaPluEKh3NMLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            # doc = 'BAACAgIAAxkBAAIFmGQ2xFqpjJnW6RKg893lTkxJndgvAAKIKgACNCKwSQEtf5jXi3IVLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            # doc = 'BAACAgIAAxkBAAIFl2Q2xDZ3xS60D7mgxRXXzcDEGaJZAAKEKgACNCKwSXxqt1knD9AKLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            doc = 'BAACAgIAAxkBAAIFm2Q2yTb2cT19kEBnst1vlWX0GZz9AAL6LAACNCK4STfB9emIRty0LwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)

@dp.message_handler(text='Регламент по уборке зала и туалетов')
async def reglament_bathroom(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обязанности кассира')
    photo7 = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_7095.JPG', 'rb')
    photo6 = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_7099.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo6)
    await bot.send_photo(message.chat.id, photo=photo7, reply_markup=markup)
    await message.answer("Молодец! Теперь ты умеешь открывать заведение. Настало время применить знания на практике. "
                         "Проинформируй своего руководителя об этом и отправь фотоотчет ему по открытию кассы, "
                         "киосков, ТВ. Короче, красавчик, дерзай! ")


@dp.message_handler(text='Обязанности кассира')
async def obyaz_kass(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/Обязанности кассира.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
async def dock_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Оформление доставки на кассе, чеки для  доставки, закрытие доставок')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/Чек-лист.xlsx', 'rb')
    doc1 = open('/home/mekan_bot/kystbay_tgbot/kst_data/Акт такси.xls', 'rb')
    await bot.send_document(message.chat.id, document=doc1)
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Оформление доставки на кассе, чеки для доставки, закрытие доставок')
async def ofor_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Скрипт кассира')
    doc = 'BAACAgIAAxkBAAIFnGQ2zNzj07FDU0syHFZvOIpdD1wEAAIOLQACNCK4Sa3QyIj2qRYrLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Скрипт кассира')
async def script_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
    doc1 = open('/home/mekan_bot/kystbay_tgbot/kst_data/Скрипт кассира.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)


@dp.message_handler(text='Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
async def konflikt_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Дополнительные обязанности кассира')
    doc1 = open('/home/mekan_bot/kystbay_tgbot/kst_data/Скрипт по отзывам.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)

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
async def close_work(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист закрытия')
    async with state.proxy() as data:
        if data['cafe'] in '1. Парина':
            file = 'BAACAgIAAxkBAAIFoGQ27frVIa5ItiQ7xfYxpYI28A89AAJbLgACNCK4SeSV9QeGec9ILwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=file, reply_markup=markup)
        elif data['cafe'] in '2. Пушкина':
            doc = 'BAACAgIAAxkBAAIFn2Q25k67BtvY8tSMMbxKr3LS48MaAALPLQACNCK4SXX1Kd0NCIR9LwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '3. Спарткавоская':
            # doc = 'BAACAgIAAxkBAAIFmGQ2xFqpjJnW6RKg893lTkxJndgvAAKIKgACNCKwSQEtf5jXi3IVLwQ'
            # await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            # await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
            await message.answer('тут материалы', reply_markup=markup)
        elif data['cafe'] in '4. Ямашева':
            doc = 'BAACAgIAAxkBAAIFnWQ21T83g9MhwzksUKsP_0Hmp6MlAAJDLQACNCK4SdM3Q6-WqXfvLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
        elif data['cafe'] in '5. Куллахметова':
            doc = 'BAACAgIAAxkBAAIFnmQ22aoZglKWqTk_DL2LJzUZeDygAAJmLQACNCK4Sd8RrjxcJU6nLwQ'
            await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
            await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Чек-лист закрытия')
async def check_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист по бытовой химии')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Чек-лист по бытовой химии')
async def chek_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Приступить к АТТЕСТАЦИИ.')
    doc1 = open('/home/mekan_bot/kystbay_tgbot/kst_data/Чек лист по бытовой химии в KSTB.pdf', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)
    await message.answer("КРАССАВИЧИК!\n"
                         "А теперь давай пройдем еще и аттестацию :) добью тебя сегодня =)", reply_markup=markup)

