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
    markup.add('Начать второй тест')
    await message.answer("Убедись, внимательно ли ты изучил составы кыстыбый, чтобы пройти тест. "
                         "Он поможет тебе закрепить изученную информацию :)\n"
                         "Успехов!", reply_markup=markup)


@dp.message_handler(text=['Начать второй тест', 'Пройти второй тест заново'])
async def start_test_2(message: types.Message):
    await UsersTest_1.two_one.set()
    await message.answer('Из чего состоит Апа?\n'
                         '\n'
                         '1. белая лепешка, копченая курица, картофельное пюре, соус чесночный, корнишоны\n'
                         '\n'
                         '2. белая лепешка, одна говяжья котлета, картофельное пюре, соус чесночный, корнишоны, '
                         'помидоры, лук\n '
                         '\n'
                         '3. черная лепешка, копченая курица, соус цезарь, салат айсбейрг, помидоры, сыр чаддер, '
                         'корнишоны, лук', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_one)
async def two_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['two_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Тамле?\n'
                                         '\n'
                                         '1. белая лепешка, соус уфтанма, картофельное пюре, соус Болоньезе\n'
                                         '\n'
                                         '2. белая лепешка, картофельное пюре, соус Болоньезе, жаренный лук\n'
                                         '\n'
                                         '3. белая лепешка, картофельное пюре, соус Болоньезе', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_two)
async def two_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['two_two'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Ак барс?\n'
                                         '\n'
                                         '1. белая лепешка, картофельное пюре, запеченая курица, жульен, соус Тар-тар\n'
                                         '\n'
                                         '2. белая лепешка, картофельное пюре, копченая курица, жульен, соус Тар-тар\n'
                                         '\n'
                                         '3. белая лепешка, картофельное пюре, запеченая курица, жульен, '
                                         'соус чесночный, '
                                         'корнишоны',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_three)
async def two_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Начать третье упражнение')
        async with state.proxy() as data:
            data['two_three'] = 'ok'
            await call.message.answer("Ты молодец, проделал(а) большую работу!\n"
                                      "Теперь ты знаешь основной состав нашего меню.\n"
                                      "Чтобы полностью усвоить зону кыстыбый, тебе надо сделать двоеное сальто вперед ("
                                      "Латнааа татарская шутка :) ", reply_markup=markup)
            await state.finish()
