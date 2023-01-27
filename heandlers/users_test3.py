from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from buttons.buttons import nmts_cb
from context.context import UsersTest_1


@dp.message_handler(text='Начать третье упражнение')
async def continue__(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Работа с оборудованиями: тепан')
    await message.answer("Вот что тебе еще надо знать о зоне кыстыбый.", reply_markup=markup)


@dp.message_handler(text='Работа с оборудованиями: тепан')
async def work_obor(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как делать заготовки.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как делать заготовки.')
async def work_zagat(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как хранить продукты.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как хранить продукты.')
async def work_prod(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как держать зону кыстыбышника в чистоте.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как держать зону кыстыбышника в чистоте.')
async def work_clean(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Изучить обязанности кыстыбшника.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Изучить обязанности кыстыбшника.')
async def work_clean(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать четвертое упражнение')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Начать четвертое упражнение')
async def continue___(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Акт списания')
    await message.answer("Дорогой друг, если у тебя остались вопросы, прошу вернутся к нужной информации и все "
                         "повторить.")
    await message.answer("А сейчас я кратко расскажу тебе про внутренний распорядок сети ресторана'Кыстыбый'",
                         reply_markup=markup)


@dp.message_handler(text='Акт списания')
async def akt_spis(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Стафф')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Стафф')
async def staff(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Рабочий чат')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Рабочий чат')
async def work_chat(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Гугл диск "КСТБ"')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Гугл диск "КСТБ"')
async def google_disc(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать третий тест')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Дорогой друг, наш первый урок подошел к концу.\n"
                         "Ты научился делать двойное сальто вперед, =)\n"
                         "изучил зону кыстыбый, внутренний распорядок, осовную часть меню. И давай с помощью теста "
                         "закрепим первый урок.", reply_markup=markup)


@dp.message_handler(text=['Начать третий тест', 'Пройти третий тест заново.'])
async def start_test_3(message: types.Message):
    await UsersTest_1.three_one.set()
    await message.answer('Что входит в состав КОМБО?\n'
                         '\n'
                         '1.\n'
                         '\n'
                         '2.\n'
                         '\n'
                         '3.\n', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_one)
async def three_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['three_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Что входит в состав ЛАНЧ?\n'
                                         '\n'
                                         '1.\n'
                                         '\n'
                                         '2.\n'
                                         '\n'
                                         '3.', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_two)
async def three_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['three_two'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Что д?\n'
                                         '\n'
                                         '1.\n'
                                         '\n'
                                         '2.\n'
                                         '\n'
                                         '3.', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_three)
async def three_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['three_three'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько грамм картофельного пюре входит в состав кыстыбый Туган?\n'
                                         '\n'
                                         '1.\n'
                                         '\n'
                                         '2.\n'
                                         '\n'
                                         '3.', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_four)
async def three_four(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['three_four'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько грамм айсберга входят в состав Батыр и Блэк татар?\n'
                                         '\n'
                                         '1.\n'
                                         '\n'
                                         '2.\n'
                                         '\n'
                                         '3.', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_five)
async def three_five(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['three_five'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text("Чем чреваты последствия, если не писать в 'Акте списания' порчу продуктов?\n"
                                         "\n"
                                         "1.\n"
                                         "\n"
                                         "2.\n"
                                         "\n"
                                         "3.", reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_six)
async def three_six(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['three_six'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text("Какая миссия компании 'Кыстыбый'\n"
                                         "\n"
                                         "1.\n"
                                         "\n"
                                         "2.\n"
                                         "\n"
                                         "3.", reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.three_seven)
async def three_six(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти третий тест заново.')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add('Приступить ко второму уроку.')
            data['three_seven'] = 'ok'
            await call.answer('Верно, ты большой молодец')
            await call.message.answer("После прохождения теста по первому уроке, напиши своему руководителю в "
                                      "ЛС, дай ему обратную связь", reply_markup=markup)
            await state.finish()
            
