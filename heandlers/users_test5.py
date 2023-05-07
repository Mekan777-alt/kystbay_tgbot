from config import dp, bot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ChatActions
from .users_test1 import works


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
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = 'BAACAgIAAxkBAAIXA2RGsB4q93TazKwM_TMxK3--dbdhAALRKQACcUg4Sg8vUP2BcBMsLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXWmRHpJeH3h-NVPZbdsHcpwz4JFXoAAKnLQACcUhASvnhV3yoOJFMLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFlGQ2v53Qy38L0xDAtPdVU34jNvDMAAJaKgACNCKwSfOwXOYS3btyLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFlWQ2wGh-TSGw2_wzIPsmjnhbCa-DAAJiKgACNCKwSb9ilm6KHdD7LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFk2Q2v3QN6n5_BHnVvGsj7C7kgEuqAAJVKgACNCKwSXG6M9WOdspKLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Как открывать и закрывать рабочую смену')
async def open_smen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие кассы и рабочей смены')
    doc = open('/root/bot/kystbay_tgbot/kst_data/e7.mp4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Открытие кассы и рабочей смены')
async def open_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с кассой')
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = 'BAACAgIAAxkBAAImdGRLs0qwoD3i2d6PGjYTKJ_08om-AALtLAAClvtZShFr5qTYAhICLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = open('/root/bot/kystbay_tgbot/kst_data/IMG_6117.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFlmQ2wxb1LiFMxrJ9LMGJ8cDu8OjrAAJ0KgACNCKwSRj4Ns4vHLhWLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = open('/root/bot/kystbay_tgbot/kst_data/IMG_6388.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIRRGRC1m7ENDAbLWMyd3FQXVPd-jBwAAJIMAAC4CEYSmPiHeD73wucLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с кассой')
async def problem_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие киосков')
    doc = open('/root/bot/kystbay_tgbot/kst_data/IMG_6390.MP4', 'rb')
    video = open('/root/bot/kystbay_tgbot/kst_data/qr.MP4', 'rb')
    video_2 = 'BAACAgIAAxkBAAI9a2RXfmrRaDKRn9iENZzJjY5oua6kAAJMJQACliHBSo_aD8lQzTusLwQ'
    video_3 = 'BAACAgIAAxkBAAI9bGRXfv9uPODYz3ftgC85iANdkFJgAAJPJQACliHBSq6288oBqL55LwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=doc)
    await bot.send_video(message.chat.id, video=video)
    await bot.send_video(message.chat.id, video=video_2)
    await bot.send_video(message.chat.id, video=video_3, reply_markup=markup)


@dp.message_handler(text='Открытие киосков')
async def open_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с киосками')
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = open('/root/bot/kystbay_tgbot/kst_data/IMG_6011.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = open('//root/bot/kystbay_tgbot/kst_data/IMG_6391.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFmGQ2xFqpjJnW6RKg893lTkxJndgvAAKIKgACNCKwSQEtf5jXi3IVLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFl2Q2xDZ3xS60D7mgxRXXzcDEGaJZAAKEKgACNCKwSXxqt1knD9AKLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = open('/root/bot/kystbay_tgbot/kst_data/открытие киосков.pptx', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с киосками')
async def problem_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Включение ТВ, экрана выдачи заказа')
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = open('/root/bot/kystbay_tgbot/kst_data/kioskparin.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFmWQ2xh-SgbsicEP7Ev921ahO8IKVAAKVKgACNCKwSRaPluEKh3NMLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIYfGRHykaUhirhCLcvwaMWVt-OfG2XAAL8LgACcUhASmQLkZZmRihCLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = open('/root/bot/kystbay_tgbot/kst_data/IMG_6390.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFmmQ2xw6ECYW1r2zVIQ6VqH2gHsR0AALgLAACNCK4ST3JnbwdjIb4LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Включение ТВ, экрана выдачи заказа')
async def vkl_vykl_tv(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент по уборке зала и туалетов')
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = 'BAACAgIAAxkBAAIXBWRGsodH7K2QWyXBHozKlQSsxeX2AALqKQACcUg4SiN9bKaZI_53LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIfE2RKkZdLMbumGmMJBbJMIzmIDP5nAAJPKwACGDBRSscpFyvfitJKLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXW2RHqZfLXt4kS_FyV36X580IneU2AALBLQACcUhAStvNRzVmta_bLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIYe2RHye27_hOb0-d98xhjeS569H77AAL5LgACcUhASkDGthVBVtBALwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFm2Q2yTb2cT19kEBnst1vlWX0GZz9AAL6LAACNCK4STfB9emIRty0LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Регламент по уборке зала и туалетов')
async def reglament_bathroom(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обязанности кассира')
    photo7 = open('/root/bot/kystbay_tgbot/kst_data/IMG_7095.JPG', 'rb')
    photo6 = open('/root/bot/kystbay_tgbot/kst_data/IMG_7099.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo6)
    await bot.send_photo(message.chat.id, photo=photo7)
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = open('/root/bot/kystbay_tgbot/kst_data/IMG_6272.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXBmRGtBoyw2aE8Z4Faaz8v7IP9DbaAAL0KQACcUg4Skjc_yiGyR8bLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXB2RGtzztlbgqt-vbDWgL400Li7nCAAIOKgACcUg4SgFsUZePdPpJLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = open('/root/bot/kystbay_tgbot/kst_data/IMG_6195.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXCGRGuCh5r3pDoWJXxtIt9diiNiWdAAIWKgACcUg4Sm0hBB5noDXELwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc)
    await message.answer("Молодец! Теперь ты умеешь открывать заведение. Настало время применить знания на практике. "
                         "Проинформируй своего руководителя об этом и отправь фотоотчет ему по открытию кассы, "
                         "киосков, ТВ. Короче, красавчик, дерзай! ", reply_markup=markup)


@dp.message_handler(text='Обязанности кассира')
async def obyaz_kass(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
    doc = open('/root/bot/kystbay_tgbot/kst_data/Обязанности кассира.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
async def dock_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Оформление доставки на кассе, чеки для доставки, закрытие доставок')
    doc = open('/root/bot/kystbay_tgbot/kst_data/Чек-лист.xlsx', 'rb')
    doc1 = open('/root/bot/kystbay_tgbot/kst_data/Акт такси.xls', 'rb')
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
    doc1 = open('/root/bot/kystbay_tgbot/kst_data/Скрипт кассира.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)


@dp.message_handler(text='Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
async def konflikt_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Закрытие смены. Чек-лист закрытия')
    doc1 = open('/root/bot/kystbay_tgbot/kst_data/Скрипт по отзывам.docx', 'rb')
    doc2 = open('/root/bot/kystbay_tgbot/kst_data/Памятка возражения.pdf', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)
    await bot.send_document(message.chat.id, document=doc2, reply_markup=markup)
    await message.answer("Ярар, хеппи енд близок, а может и нет)))Хихихихииииии:D Все уже, заканчиваем. Почти))")
    await message.answer("Давай научимся закрывать смену. Администратор вечером сам закроет кассу, киоски и сделает "
                         "отчет по выручке дня, поэтому тебе нужно будет совместно с командой сдать чистую смену, "
                         "выключить оборудования, свет, поставить на сигнализацию кафе и заполнить чек-лист закрытия "
                         "по чистоте. Здесь тебе будет не сложно")


@dp.message_handler(text='Закрытие смены. Чек-лист закрытия')
async def close_work(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист закрытия')
    if works['cafe'] in '1. Парина' and works['id'] == message.chat.id:
        file = 'BAACAgIAAxkBAAIFoGQ27frVIa5ItiQ7xfYxpYI28A89AAJbLgACNCK4SeSV9QeGec9ILwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFn2Q25k67BtvY8tSMMbxKr3LS48MaAALPLQACNCK4SXX1Kd0NCIR9LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIXXGRHqosockJCjdR4mpjYO_s8SiXrAALHLQACcUhASiBYn4pxtT7rLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFnWQ21T83g9MhwzksUKsP_0Hmp6MlAAJDLQACNCK4SdM3Q6-WqXfvLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова' and works['id'] == message.chat.id:
        doc = 'BAACAgIAAxkBAAIFnmQ22aoZglKWqTk_DL2LJzUZeDygAAJmLQACNCK4Sd8RrjxcJU6nLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Чек-лист закрытия')
async def check_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист по бытовой химии')
    doc1 = open('/root/bot/kystbay_tgbot/kst_data/Чек-лист Закрытия1.docx', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)


@dp.message_handler(text='Чек-лист по бытовой химии')
async def chek_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Приступить к АТТЕСТАЦИИ.')
    doc1 = open('/root/bot/kystbay_tgbot/kst_data/Чек лист по бытовой химии в KSTB.pdf', 'rb')
    await bot.send_document(message.chat.id, document=doc1, reply_markup=markup)
    await message.answer("КРАССАВИЧИК!\n"
                         "А теперь давай пройдем еще и аттестацию :) добью тебя сегодня =)", reply_markup=markup)
