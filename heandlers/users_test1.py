from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from context.context import UsersTest_1
from buttons.buttons import nmts_cb


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, друг! с тобой на связи KSTBOT, я обучу тебя всей работе в нашей компании. \n'
                         'Для начала ознакомься с инструкцией как со мной работать и особенно удели внимание '
                         'по работе с поисковиком, иначе я не правильно отвечу на твой вопрос...')
    await message.answer("Давай знакомиться, напиши как тебя зовут.")
    await UsersTest_1.name.set()


@dp.message_handler(state=UsersTest_1.name)
async def command_name(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать обучение')
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer(f'Приятно познакомиться, {message.text}, посмотри приветсвенное видео с '
                             'основателем "Кыстыбый" - Азатом.', reply_markup=markup)
        await state.finish()


@dp.message_handler(text='Начать обучение', state=None)
async def start_education(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я понял(а), продолжим обучение.')
    await message.answer('Первый урок.\n'
                         '\n'
                         'Приступим к первому уроку. Я предоставлю тебе материалы в PDF формате и видеороликах.\n'
                         'Для закрепления информации ты будешь проходить тесты.')
    await message.answer("Начнем с первой темы 'Внешний вид на рабочем месте'", reply_markup=markup)


@dp.message_handler(text='Я понял(а), продолжим обучение.')
async def i_undestand(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Парина')
    markup.add('2. Пушкина')
    markup.add('3. Спарткавоская')
    markup.add('4. Ямашева')
    markup.add('5. Куллахметова')
    await message.answer("Выбери свою точку", reply_markup=markup)


@dp.message_handler(text='1. Парина')
async def parina(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='2. Пушкина')
async def pushkina(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='3. Спарткавоская')
async def spart(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='4. Ямашева')
async def yamash(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='5. Куллахметова')
async def kullah(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='Я посмотрел(а), го дальше :)')
async def done_video(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :).')
    await message.answer("А Сейчас мы с тобой изучим меню по разделам", reply_markup=markup)
    await message.answer('Тут тоже видео и материалы')


@dp.message_handler(text='Я посмотрел(а), го дальше :).')
async def done_video_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    await message.answer("Давай рассмотрим составы кыстыбышек в наборе 'Комбо'", reply_markup=markup)


@dp.message_handler(text='1. Чип чеби')
async def chip(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('2. Алтын чеби')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='2. Алтын чеби')
async def altyn(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('3. Кояш')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='3. Кояш')
async def koyash(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('4. Батыр')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='4. Батыр')
async def batyr(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('5. Блэк Татар')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='5. Блэк Татар')
async def black_tatar(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('6. Су анасы')
    await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='6. Су анасы')
async def su_anasy(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать тест')
    await message.answer("Убедись, внимательно ли ты изучил составы кыстыбый, чтобы пройти тест. "
                         "Он поможет тебе закрепить изученную информацию :)\n"
                         "Успехов!", reply_markup=markup)


@dp.message_handler(text=['Начать тест', 'Пройти тест заново'])
async def start_test(message: types.Message):
    await message.answer('Из чего состоит Батыр?\n'
                         '\n'
                         '1. белая лепешка, одна говяжья котлета, сыр адыгейский, соус бургер, айсберг, '
                         'помидоры, '
                         'корнишоны, лук\n'
                         '\n'
                         '2. белая лепешка, одна говяжья котлета, соус барбекю, салат айсбейрг, помидоры, '
                         'сыр чаддер, '
                         'корнишоны, лук\n'
                         '\n'
                         '3. черная лепешка, две говяжьи котлеты, соус цезарь, салат айсбейрг, помидоры, '
                         'сыр чаддер, '
                         'корнишоны, лук', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_one)
async def one_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['one_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Су Анасы?\n'
                                         '\n'
                                         '1. белая лепешка, рис, соус тереяки, лосось, нори, свежий огурец\n'
                                         '2. белая лепешка, рис, соус тереяки, наггенсы, нори, корнишоны\n'
                                         '3. белая лепешка, рис, соус бургер, лосось, нори, свежий огурец',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_two)
async def one_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['one_two'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Чип Чеби?\n'
                                         '\n'
                                         '1. белая лепешка, одна куриная котлета, соус уфтанма, айсберг, корнишоны и '
                                         'помидоры\n '
                                         '\n'
                                         '2. белая лепешка, одна говяжья котлета, соус бургер, айсберг, корнишоны, '
                                         'помидоры и '
                                         'лук\n '
                                         '\n'
                                         '3. белая лепешка, одна куриная котлета, соус бургер, айсберг и помидоры',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.one_three)
async def one_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Продолжить обучение')
        async with state.proxy() as data:
            data['one_three'] = 'ok'
            await call.message.answer('Верно! едем дальше', reply_markup=markup)
            await state.finish()
