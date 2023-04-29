from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ChatActions
from buttons.buttons import nmts_cb, nmts_cb2
from context.context import UsersTest_1
from .users_test1 import works


@dp.message_handler(text='Начать третье упражнение')
async def continue__(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Зона кыстыбый')
    await message.answer("Вот что тебе еще надо знать о зоне кыстыбый.", reply_markup=markup)


@dp.message_handler(text='Зона кыстыбый')
async def work_obor(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как делать заготовки.')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/zonakyst.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video, reply_markup=markup)


@dp.message_handler(text='Как делать заготовки.')
async def work_zagat(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обзор холодильников')
    video2 = 'BAACAgIAAxkBAAIZAWRIFXs7kt1sqaCQrHer01y9aZA6AAJrMwACcUhASvFGPcbzv87ILwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video2, reply_markup=markup)


@dp.message_handler(text='Обзор холодильников')
async def work_prod(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как держать зону кыстыбышника в чистоте.')
    if works['cafe'] in '1. Парина':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_8163.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина':
        doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_8162.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская':
        doc = 'BAACAgIAAxkBAAIXAmRGrkDq-jLJJoZEbnLHSPIjyNFEAALKKQACcUg4Su2q2tbGQi3XLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева':
        doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_8164.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова':
        doc = 'BAACAgIAAxkBAAIXAWRGrLrlcsVvhkjYZjQnFy3OBrvhAALAKQACcUg4SiHPIgMXhS0aLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Как держать зону кыстыбышника в чистоте.')
async def work_clean(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обязанности кыстыбышника')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/chistotakst.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='Обязанности кыстыбышника')
async def work_clean(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать четвертое упражнение')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/Обязанности кыстыбышника.docx', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_document(chat_id=message.chat.id, document=video, reply_markup=markup)


@dp.message_handler(text='Начать четвертое упражнение')
async def continue___(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Акт списания')
    await message.answer("Дорогой друг, если у тебя остались вопросы, прошу вернутся к нужной информации и все "
                         "повторить.")
    await message.answer("А сейчас я кратко расскажу тебе про внутренний распорядок сети ресторана 'Кыстыбый'",
                         reply_markup=markup)


@dp.message_handler(text='Акт списания')
async def akt_spis(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Стафф')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/aktspis.xlsx', 'rb')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/aktspisa.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video, reply_markup=markup)
    await bot.send_document(message.chat.id, document=doc)


@dp.message_handler(text='Стафф')
async def staff(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Рабочий чат')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/staff.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video, reply_markup=markup)


@dp.message_handler(text='Рабочий чат')
async def work_chat(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать тест к первому уроку')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/char_rab.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(chat_id=message.chat.id, video=video, reply_markup=markup)
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await message.answer("Дорогой друг, наш первый урок подошел к концу.\n"
                         "Ты научился делать двойное сальто вперед, =)\n"
                         "изучил зону кыстыбый, внутренний распорядок, основную часть меню. И давай с помощью теста "
                         "закрепим первый урок.", reply_markup=markup)


@dp.message_handler(text=['Начать тест к первому уроку', 'Пройти первый тест заново'])
async def start_test(message: types.Message):
    await UsersTest_1.one_1.set()
    await message.answer('Что входит в состав КОМБО?\n'
                         '\n'
                         '1. кыстыбый, напиток морс/компот, картошка фри\n'
                         '\n'
                         '2. кыстыбый, чай, суп тыквенный \n'
                         '\n'
                         '3. кыстыбый, напиток газированный 0,5, картошка фри', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_1)
async def one_1(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['one_1'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Что входит в состав ЛАНЧ?\n'
                                         '\n'
                                         '1. Кыстыбый с пюре, суп лапша\n'
                                         '2. Кыстыбый со свежими овощами, суп лапша\n'
                                         '3. Кыстыбый с основой пюре, чай 0,3, суп лапша',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_2)
async def one_2(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['one_2'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит форма сотрудника?\n'
                                         '\n'
                                         '1. чистая футболка от компании «КСТБ», желтые брюки, вторая закрытая обувь, '
                                         'бейджик, козырек «КСТБ» (кепка)\n '
                                         '\n'
                                         '2. чистая футболка от компании «КСТБ», черные брюки, вторая закрытая обувь, '
                                         'бейджик, козырек «КСТБ» (кепка)\n '
                                         '\n'
                                         '3. чистая футболка от компании «КСТБ», черные брюки, вторая закрытая обувь, '
                                         'бейджик, сетка для волос, козырек «КСТБ» (кепка)',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_3)
async def one_3(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['one_3'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько грамм картофельного пюре входит в состав кыстыбый Туган?\n'
                                         '\n'
                                         '1. 125 гр\n '
                                         '\n'
                                         '2. 175 гр\n '
                                         '\n'
                                         '3. 180 гр',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_4)
async def one_4(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['one_4'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько грамм айсберга входят в состав Батыр и Блэк Татар?\n'
                                         '\n'
                                         '1. 30 гр, 15 гр\n '
                                         '\n'
                                         '2. 40 гр, 15 гр\n '
                                         '\n'
                                         '3. 15 гр, 15 гр',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_5)
async def one_5(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['one_5'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Чем чреваты последствия, если не писать в «Акте списания» порчу продуктов?\n'
                                         '\n'
                                         '1. отобразиться недосдача в период инвентаризации. Команда будет нести '
                                         'определенные последствия\n '
                                         '\n'
                                         '2. увольнение \n '
                                         '\n',
                                         reply_markup=nmts_cb2())


@dp.callback_query_handler(text=['1', '2'], state=UsersTest_1.one_6)
async def one_6(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['one_6'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Какая миссия компании «Кыстыбый»?\n'
                                         '\n'
                                         '1. халяль еда, укрепление семейных уз\n '
                                         '\n'
                                         '2. отдых, укрепление семейных уз, улыбка\n '
                                         '\n'
                                         '3. халяль еда, укрепление семейных уз, улыбка',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_7)
async def one_7(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Приступить ко второму уроку.')
        async with state.proxy() as data:
            data['one_7'] = 'ok'
            await call.message.answer('Верно! едем дальше', reply_markup=markup)
            await state.finish()
