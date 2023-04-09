from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
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
async def open_smen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие кассы и рабочей смены')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие кассы и рабочей смены')
async def open_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с кассой')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с кассой')
async def problem_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Открытие киосков')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Открытие киосков')
async def open_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с киосками')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с киосками')
async def problem_kiosk(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Включение ТВ, экрана выдачи заказа')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Включение ТВ, экрана выдачи заказа')
async def vkl_vykl_tv(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Проблемы в работе с ТВ, экрана выдачи заказа')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Проблемы в работе с ТВ, экрана выдачи заказа')
async def problem_vkl_vykl_tv(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент по уборке зала и туалетов')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Регламент по уборке зала и туалетов')
async def reglament_bathroom(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Обязанности кассира')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Молодец! Теперь ты умеешь открывать заведение. Настало время применить знания на практике. "
                         "Проинформируй своего руководителя об этом и отправь фотоотчет ему по открытию кассы, "
                         "киосков, ТВ. Короче, красавчик, дерзай! ")


@dp.message_handler(text='Обязанности кассира')
async def obyaz_kass(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Нужные документы для кассира, как чек-лист, акт такси, график уборки туалета')
async def dock_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Оформление доставки на кассе, чеки для  доставки, закрытие доставок')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Оформление доставки на кассе, чеки для  доставки, закрытие доставок')
async def ofor_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Скрипт кассира')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Скрипт кассира')
async def script_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как решать конфликтные вопросы с гостями? Скрипт по отзывам.')
async def konflikt_kassa(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Дополнительные обязанности кассира')
    await message.answer('тут материалы', reply_markup=markup)


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


@dp.message_handler(text='Закрытие смены. Чек-лист закрытия')
async def close_work(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чек-лист по бытовой химии')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Чек-лист по бытовой химии')
async def chek_list(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент заполнение маркетов')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Регламент заполнение маркетов')
async def reglament_maket(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент заполнения витрины')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Регламент заполнения витрины')
async def reglament_vitrin(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать пятый тест')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Теперь приступим к тесту по третьему уроку. Я для тебя постарался максимально объяснить все "
                         "детали твоей работы. Если у тебя остались вопросы, обязательно обратись к своему наставнику "
                         "и все уточни)) Блиииин, я тобою горжусь!")


@dp.message_handler(text=['Начать пятый тест', 'Пройти пятый тест заново'])
async def test_5(message: types.Message):
    await UsersTest_1.five_one.set()
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


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.five_one)
async def five_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
    elif call.data == '2':
        async with state.proxy() as data:
            data['five_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Су Анасы?\n'
                                         '\n'
                                         '1. белая лепешка, рис, соус тереяки, лосось, нори, свежий огурец\n'
                                         '2. белая лепешка, рис, соус тереяки, наггенсы, нори, корнишоны\n'
                                         '3. белая лепешка, рис, соус бургер, лосось, нори, свежий огурец',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.five_two)
async def five_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
    elif call.data == '1':
        async with state.proxy() as data:
            data['five_two'] = 'ok'
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


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.five_three)
async def five_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти первый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Приступить к АТТЕСТАЦИИ.')
        async with state.proxy() as data:
            data['five_three'] = 'ok'
            await call.message.answer('Верно! едем дальше', reply_markup=markup)
            await call.message.answer("КРАССАВИЧИК!\n"
                                      "А теперь давай пройдем еще и аттестацию :) добью тебя сегодня =)",
                                      reply_markup=markup)
