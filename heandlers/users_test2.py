from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from context.context import Users


@dp.message_handler(text='Продолжить обучение')
async def continue_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Туган')
    markup.add('2. Тамле')
    markup.add('3. Абый')
    markup.add('4. Гомбэ')
    markup.add('5. Апа')
    markup.add('6. Ак барс')
    await message.answer("Давай рассмотрим еще составы кыстыбышек в наборе 'Ланч'", reply_markup=markup)


@dp.message_handler(text='1. Туган')
async def tugan(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('2. Тамле')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='2. Тамле')
async def tamle(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('3. Абый')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='3. Абый')
async def aby(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('4. Гомбэ')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='4. Гомбэ')
async def gombe(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('5. Апа')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='5. Апа')
async def apa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('6. Су анасы')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='6. Ак барс')
async def ak_bars(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать тест')
    await message.answer("Убедись, внимательно ли ты изучил составы кыстыбый, чтобы пройти тест. "
                         "Он поможет тебе закрепить изученную информацию :)\n"
                         "Успехов!", reply_markup=markup)


@dp.message_handler(text=['Начать тест', 'Пройти тест заново'])
async def start_test_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1')
    markup.add('2')
    markup.add('3')
    await Users.two_one.set()
    await message.answer('Из чего состоит Апа?\n'
                         '\n'
                         '1. белая лепешка, копченая курица, картофельное пюре, соус чесночный, корнишоны\n'
                         '\n'
                         '2. белая лепешка, одна говяжья котлета, картофельное пюре, соус чесночный, корнишоны, '
                         'помидоры, лук\n '
                         '\n'
                         '3. черная лепешка, копченая курица, соус цезарь, салат айсбейрг, помидоры, сыр чаддер, '
                         'корнишоны, лук', reply_markup=markup)


@dp.message_handler(text=['1', '2', '3'], state=Users.two_one)
async def two_one(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '2' or message.text == '3':
        markup.add('Пройти тест заново')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '1':
        markup.add('1')
        markup.add('2')
        markup.add('3')
        async with state.proxy() as data:
            data['two_one'] = 'ok'
            await Users.next()
            await message.answer('Верно, едем дальше')
            await message.answer('Из чего состоит Тамле?\n'
                                 '\n'
                                 '1. белая лепешка, соус уфтанма, картофельное пюре, соус Болоньезе\n'
                                 '\n'
                                 '2. белая лепешка, картофельное пюре, соус Болоньезе, жаренный лук\n'
                                 '\n'
                                 '3. белая лепешка, картофельное пюре, соус Болоньезе', reply_markup=markup)


@dp.message_handler(text=['1', '2', '3'], state=Users.two_two)
async def two_two(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '1' or message.text == '2':
        markup.add('Пройти тест заново')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '3':
        markup.add('1')
        markup.add('2')
        markup.add('3')
        async with state.proxy() as data:
            data['two_two'] = 'ok'
            await Users.next()
            await message.answer('Верно, едем дальше')
            await message.answer('Из чего состоит Ак барс?\n'
                                 '\n'
                                 '1. белая лепешка, картофельное пюре, запеченая курица, жульен, соус Тар-тар\n'
                                 '\n'
                                 '2. белая лепешка, картофельное пюре, копченая курица, жульен, соус Тар-тар\n'
                                 '\n'
                                 '3. белая лепешка, картофельное пюре, запеченая курица, жульен, соус чесночный, '
                                 'корнишоны',
                                 reply_markup=markup)


@dp.message_handler(text=['1', '2', '3'], state=Users.two_three)
async def two_three(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '2' or message.text == '3':
        markup.add('Пройти тест заново')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '1':
        markup.add('Продолжить обучение.')
        markup.add('Назад')
        async with state.proxy() as data:
            data['two_three'] = 'ok'
            await message.answer("Ты молодец, проделал(а) большую работу!\n"
                                 "Теперь ты знаешь основной состав нашего меню.\n"
                                 "Чтобы полностью усвоить зону кыстыбый, тебе надо сделать двоеное сальто вперед ("
                                 "Латнааа татарская шутка :) ", reply_markup=markup)
            await state.finish()


@dp.message_handler(text='Продолжить обучение.')
async def continue__(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Работа с оборудованиями: тепан')
    markup.add('Как делать заготовки.')
    markup.add('Как хранить продукты.')
    markup.add('Как держать зону кыстыбышника в чистоте.')
    markup.add('Изучить обязанности кыстыбшника.')
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
    markup.add('Продолжить обучение..')
    markup.add('Назад')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Продолжить обучение..')
async def continue___(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Акт списания')
    markup.add('Стафф')
    markup.add('Рабочий чат')
    markup.add('Гугл диск "КСТБ"')
    await message.answer("Дорогой друг, если у тебя остались вопросы, прошу вернутся к нужной информации и все "
                         "повторить.")
    await message.answer("А сейчас я кратко расскажу тебе про внутренний распорядок сети ресторана'Кыстыбый'")


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
    markup.add()
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Дорогой друг, наш первый урок подошел к концу.\n"
                         "Ты научился делать двойное сальто вперед, =)\n"
                         "изучил зону кыстыбый, внутренний распорядок, осовную часть меню. И давай с помощью теста "
                         "закрепим первый урок.", reply_markup=markup)