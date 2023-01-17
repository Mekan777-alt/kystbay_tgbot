from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from context.context import Users


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, друг! с тобой на связи KSTBOT, я обучу тебя всей работе в нашей компании. \n'
                         'Для начала ознакомься с инструкцией как со мной работать и особенно удели внимание '
                         'по работе с поисковиком, иначе я не правильно отвечу на твой вопрос...')
    await message.answer("Давай знакомиться, напиши как тебя зовут.")


@dp.message_handler(text='12')
async def command_name(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать обучение')
    await message.answer('Приятно познакомиться, (Имя), посмотри приветсвенное видео с '
                         'основателем "Кыстыбый" - Азатом.', reply_markup=markup)


@dp.message_handler(text='Начать обучение')
async def start_education(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я понял(а), продолжим обучение.')
    await message.answer('Первый урок.\n'
                         '\n'
                         'Приступим к первому уроку. Я предоставлю тебе материалы в PDF формате и видеороликах.\n'
                         'Для закрепления информации ты будешь проходить тесты.')
    await message.answer("Начнем с первой темы 'Внешний вид на рабочем месте'", reply_markup=markup)


@dp.message_handler(text='Я понял(а), продолжим обучение.', state=None)
async def i_undestand(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Парина')
    markup.add('2. Пушкина')
    markup.add('3. Спарткавоская')
    markup.add('4. Ямашева')
    markup.add('5. Куллахметова')
    await Users.street.set()
    await message.answer("Выбери свою точку", reply_markup=markup)


@dp.message_handler(text='1. Парина', state=Users.street)
async def parina(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['street'] = message.text
        await Users.next()
        await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='2. Пушкина', state=Users.street)
async def pushkina(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['street'] = message.text
        await Users.next()
        await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='3. Спарткавоская', state=Users.street)
async def spart(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['street'] = message.text
        await Users.next()
        await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='4. Ямашева', state=Users.street)
async def yamash(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['street'] = message.text
        await Users.next()
        await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='5. Куллахметова', state=Users.street)
async def kullah(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :)')
    async with state.proxy() as data:
        data['street'] = message.text
        await Users.next()
        await message.answer('Тут видео и файл', reply_markup=markup)


@dp.message_handler(text='Я посмотрел(а), го дальше :)', state=Users.video_1)
async def done_video(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я посмотрел(а), го дальше :).')
    async with state.proxy() as data:
        data['video_1'] = 'done'
        await Users.next()
        await message.answer("А Сейчас мы с тобой изучим меню по разделам", reply_markup=markup)
        await message.answer('Тут тоже видео и материалы')


@dp.message_handler(text='Я посмотрел(а), го дальше :).', state=Users.video_2)
async def done_video_2(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('2. Алтын чеби')
    markup.add('3. Кояш')
    markup.add('4. Батыр')
    markup.add('5. Блэк Татар')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['video_2'] = 'done'
        await Users.next()
        await message.answer("Давай рассмотрим составы кыстыбышек в наборе 'Комбо'", reply_markup=markup)


@dp.message_handler(text='1. Чип чеби', state=Users.one)
async def chip(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('2. Алтын чеби')
    markup.add('3. Кояш')
    markup.add('4. Батыр')
    markup.add('5. Блэк Татар')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['one'] = message.text
        await Users.next()
        await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='2. Алтын чеби', state=Users.two)
async def altyn(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('3. Кояш')
    markup.add('4. Батыр')
    markup.add('5. Блэк Татар')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['two'] = message.text
        await Users.next()
        await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='3. Кояш', state=Users.three)
async def koyash(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('2. Алтын чеби')
    markup.add('4. Батыр')
    markup.add('5. Блэк Татар')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['three'] = message.text
        await Users.next()
        await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='4. Батыр', state=Users.four)
async def batyr(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('2. Алтын чеби')
    markup.add('3. Кояш')
    markup.add('5. Блэк Татар')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['four'] = message.text
        await Users.next()
        await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='5. Блэк Татар', state=Users.five)
async def black_tatar(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('2. Алтын чеби')
    markup.add('3. Кояш')
    markup.add('4. Батыр')
    markup.add('6. Су анасы')
    async with state.proxy() as data:
        data['five'] = message.text
        await Users.next()
        await message.answer('тут меняем клаву', reply_markup=markup)


@dp.message_handler(text='6. Су анасы', state=Users.six)
async def su_anasy(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1. Чип чеби')
    markup.add('2. Алтын чеби')
    markup.add('3. Кояш')
    markup.add('4. Батыр')
    markup.add('5. Блэк Татар')
    async with state.proxy() as data:
        data['six'] = message.text
        await message.answer("Убедись, внимательно ли ты изучил составы кыстыбый, чтобы пройти тест. "
                             "Он поможет тебе закрепить изученную информацию :)\n"
                             "Успехов!")
