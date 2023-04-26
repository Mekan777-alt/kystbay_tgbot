from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ChatActions
from context.context import UsersTest_1

works = []


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, друг! с тобой на связи KSTBOT, я обучу тебя всей работе в нашей компании. \n')
    await message.answer("Давай знакомиться, напиши как тебя зовут.")
    await UsersTest_1.name.set()


@dp.message_handler(state=UsersTest_1.name)
async def command_name(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать обучение')
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer(f'Приятно познакомиться, {message.text}, посмотри приветсвенное видео '
                             ' с Основателем Кыстыбый - Назмутдинов Азатом и с руководителем сети Еленой Кофоновой',
                             reply_markup=markup)
        video = "BAACAgIAAxkBAAMHZDAGxfiTTc-0WpjY1Kg0Kjz2tdQAArcxAAK0MYFJNbrtrYo39A8vBA"
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='Начать обучение')
async def start_education(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я понял(а), продолжим обучение.')
    await message.answer('Первый урок.\n'
                         '\n'
                         'Приступим к первому уроку. Я предоставлю тебе материалы в PDF формате и видеороликах.\n'
                         'Для закрепления информации ты будешь проходить тесты.')
    await message.answer("Начнем с первой темы 'Внешний вид на рабочем месте'", reply_markup=markup)
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/vneshniyvid.MP4', 'rb')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/forma.pptx', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video)
    await bot.send_document(message.chat.id, document=doc)


@dp.message_handler(text='Я понял(а), продолжим обучение.')
async def i_undestand(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Парина')
    markup.add('2. Пушкина')
    markup.add('3. Спартаковская')
    markup.add('4. Ямашева')
    markup.add('5. Кулахметова')
    await UsersTest_1.cafe.set()
    await message.answer("Выбери свою точку", reply_markup=markup)


@dp.message_handler(text='1. Парина', state=UsersTest_1.cafe)
async def parina(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['cafe'] = message.text
        await state.finish()
        file = "BAACAgIAAxkBAAMGZDACavgOKYb2Uce9QCTW0aZvkh4AAqQxAAK0MYFJqvztuhQf-OgvBA"
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='2. Пушкина', state=UsersTest_1.cafe)
async def pushkina(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['cafe'] = message.text
        await state.finish()
        file = "BAACAgIAAxkBAAMcZDAIzYEnZUnQt3nc8exVVmvrFz8AAsExAAK0MYFJ_o9QSoIF2xkvBA"
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='3. Спартаковская', state=UsersTest_1.cafe)
async def spart(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['cafe'] = message.text
        await state.finish()
        file = "BAACAgIAAxkBAAIBP2QxqtK-k5NXmIZH-WS-sBoG7720AAJlKwACtHKRSfxxkjNzDs-uLwQ"
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='4. Ямашева', state=UsersTest_1.cafe)
async def yamash(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['cafe'] = message.text
        await state.finish()
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/yamash.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='5. Кулахметова', state=UsersTest_1.cafe)
async def kullah(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['cafe'] = message.text
        await state.finish()
        file = "BAACAgIAAxkBAAIBPmQxnIhXITqL8KthUK7nuf1Bs9a4AAL4KgACtHKRSR5fKtmcOj4ELwQ"
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(chat_id=message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Я посмотрел(а), го дальше :)')
async def done_video(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :).')
    await message.answer("А Сейчас мы с тобой изучим меню по разделам", reply_markup=markup)
    photo1 = open('/home/mekan_bot/kystbay_tgbot/kst_data/biznes.JPG', 'rb')
    photo2 = open('/home/mekan_bot/kystbay_tgbot/kst_data/detskoye.PNG', 'rb')
    photo3 = open('/home/mekan_bot/kystbay_tgbot/kst_data/kombonabory.JPG', 'rb')
    photo4 = open('/home/mekan_bot/kystbay_tgbot/kst_data/napitki.PNG', 'rb')
    photo5 = open('/home/mekan_bot/kystbay_tgbot/kst_data/pervyybluda.JPG', 'rb')
    photo6 = open('/home/mekan_bot/kystbay_tgbot/kst_data/salaty.JPG', 'rb')
    photo7 = open('/home/mekan_bot/kystbay_tgbot/kst_data/deserty.JPG', 'rb')
    photo8 = open('/home/mekan_bot/kystbay_tgbot/kst_data/sneki.JPG', 'rb')
    photo9 = open('/home/mekan_bot/kystbay_tgbot/kst_data/vtorybluda.JPG', 'rb')
    photo10 = open('/home/mekan_bot/kystbay_tgbot/kst_data/vypechka.JPG', 'rb')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/zawtraki.pdf', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.chat.id, photo=photo5)
    await bot.send_photo(message.chat.id, photo=photo9)
    await bot.send_photo(message.chat.id, photo=photo4)
    await bot.send_photo(message.chat.id, photo=photo6)
    await bot.send_photo(message.chat.id, photo=photo7)
    await bot.send_photo(message.chat.id, photo=photo8)
    await bot.send_photo(message.chat.id, photo=photo10)
    await bot.send_photo(message.chat.id, photo=photo1)
    await bot.send_photo(message.chat.id, photo=photo2)
    await bot.send_photo(message.chat.id, photo=photo3)
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Я посмотрел(а), го дальше :).')
async def done_video_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    await message.answer("Давай рассмотрим составы кыстыбышек в наборе 'Комбо'", reply_markup=markup)


@dp.message_handler(text='1. Чип чеби')
async def chip(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/chipchebi.JPG', 'rb')
    markup.add('2. Алтын чеби')
    video = 'BAACAgIAAxkBAAIRRWRDEFGKTdRzg7_h9zxsFqHTj6WZAAJOLQACXmgZSrBbFtMYyleULwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='2. Алтын чеби')
async def altyn(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('3. Кояш')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/altynchebi.PNG', 'rb')
    video = 'BAACAgIAAxkBAAIRRmRDEXU-9LBVpZgxwrKQ442Ga4E4AAJULQACXmgZSvbFRyfYaVrGLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='3. Кояш')
async def koyash(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('4. Батыр')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/koyash.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRR2RDEhXtthaSP-CjlmWOzUqu5euMAAJVLQACXmgZSg45y0MOQI1CLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='4. Батыр')
async def batyr(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('5. Блэк Татар')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/batyr.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRSGRDErCXgVjC5fD9ZNvfTTVMnv_YAAJWLQACXmgZSjxRL2SJc2PQLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='5. Блэк Татар')
async def black_tatar(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('6. Су анасы')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/blacktatar.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRSWRDFID8tO_yKEqdD87_VQYCsodhAAJXLQACXmgZSvlff7zUB-FSLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)


@dp.message_handler(text='6. Су анасы')
async def su_anasy(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать второе упражнение')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/suanasy.JPG', 'rb')
    video = 'BAACAgIAAxkBAAIRSmRDF2Hg6D0qDT59vq8730VvIcg5AAJZLQACXmgZSvRmQnKMFNqXLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)
    await bot.send_video(chat_id=message.chat.id, video=video)
