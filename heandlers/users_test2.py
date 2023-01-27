from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from context.context import UsersTest_1


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
    markup.add('Начать второй тест')
    await message.answer("Убедись, внимательно ли ты изучил составы кыстыбый, чтобы пройти тест. "
                         "Он поможет тебе закрепить изученную информацию :)\n"
                         "Успехов!", reply_markup=markup)


@dp.message_handler(text=['Начать второй тест', 'Пройти тест заново.'])
async def start_test_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1')
    markup.add('2')
    markup.add('3')
    await UsersTest_1.two_one.set()
    await message.answer('Из чего состоит Апа?\n'
                         '\n'
                         '1. белая лепешка, копченая курица, картофельное пюре, соус чесночный, корнишоны\n'
                         '\n'
                         '2. белая лепешка, одна говяжья котлета, картофельное пюре, соус чесночный, корнишоны, '
                         'помидоры, лук\n '
                         '\n'
                         '3. черная лепешка, копченая курица, соус цезарь, салат айсбейрг, помидоры, сыр чаддер, '
                         'корнишоны, лук', reply_markup=markup)


@dp.message_handler(text=['1', '2', '3'], state=UsersTest_1.two_one)
async def two_one(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '2' or message.text == '3':
        markup.add('Пройти тест заново.')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '1':
        markup.add('1')
        markup.add('2')
        markup.add('3')
        async with state.proxy() as data:
            data['two_one'] = 'ok'
            await UsersTest_1.next()
            await message.answer('Верно, едем дальше')
            await message.answer('Из чего состоит Тамле?\n'
                                 '\n'
                                 '1. белая лепешка, соус уфтанма, картофельное пюре, соус Болоньезе\n'
                                 '\n'
                                 '2. белая лепешка, картофельное пюре, соус Болоньезе, жаренный лук\n'
                                 '\n'
                                 '3. белая лепешка, картофельное пюре, соус Болоньезе', reply_markup=markup)


@dp.message_handler(text=['1', '2', '3'], state=UsersTest_1.two_two)
async def two_two(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '1' or message.text == '2':
        markup.add('Пройти тест заново.')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '3':
        markup.add('1')
        markup.add('2')
        markup.add('3')
        async with state.proxy() as data:
            data['two_two'] = 'ok'
            await UsersTest_1.next()
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


@dp.message_handler(text=['1', '2', '3'], state=UsersTest_1.two_three)
async def two_three(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '2' or message.text == '3':
        markup.add('Пройти тест заново.')
        await message.answer('Тест провален:\n'
                             'Все заново', reply_markup=markup)
        await state.finish()
    elif message.text == '1':
        markup.add('Продолжить обучение.')
        async with state.proxy() as data:
            data['two_three'] = 'ok'
            await message.answer("Ты молодец, проделал(а) большую работу!\n"
                                 "Теперь ты знаешь основной состав нашего меню.\n"
                                 "Чтобы полностью усвоить зону кыстыбый, тебе надо сделать двоеное сальто вперед ("
                                 "Латнааа татарская шутка :) ", reply_markup=markup)
            await state.finish()
