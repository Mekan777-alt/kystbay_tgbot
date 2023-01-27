from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from buttons.buttons import nmts_cb
from context.context import UsersTest_1


@dp.message_handler(text='Приступить к АТТЕСТАЦИИ.')
async def start_attestation(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать онлайн АТТЕСТАЦИЮ')
    await message.answer("Вот и настало время Аттестации. Будь спокоен, ведь всю важную информацию ты уже усвоил. "
                         "Повтори то, что ты плохо запомнил. Теперь выдохни!)) Ты усвоил столько навыков в "
                         "сети-ресторанов 'KSTB', я тебя поздравляю!!! После прохождения онлайн-аттестации сообщи об "
                         "этом своему руководителю.", reply_markup=markup)


@dp.message_handler(text='Начать онлайн АТТЕСТАЦИЮ')
async def online_attestation(message: types.Message):
    await UsersTest_1.attestation_one.set()
    await message.answer('Какой состав Кыстыбый Алтын?\n'
                         '\n'
                         '1. Лепешка, айсберг, помидоры, корнишоны, лук красный, 4 наггетса, соус чесночный\n'
                         '\n'
                         '2. Лепешка, айсберг, помидоры, корнишоны, лук красный, 2 наггетса пополам, соус цезарь\n'
                         '\n'
                         '3. Лепешка, айсберг, помидоры, корнишоны, жаренный лук, 1 наггетса попалам',
                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.attestation_one)
async def attestat_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти аттестацию заново')
        await call.message.answer('Аттестация провалена:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['attestation_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Су Анасы?\n'
                                         '\n'
                                         '1. белая лепешка, рис, соус тереяки, лосось, нори, свежий огурец\n'
                                         '2. белая лепешка, рис, соус тереяки, наггенсы, нори, корнишоны\n'
                                         '3. белая лепешка, рис, соус бургер, лосось, нори, свежий огурец',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.attestation_two)
async def attestat_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти аттестацию заново')
        await call.message.answer('Аттестация провалена:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['attestation_two'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Состав КОМБО №3?\n'
                                         '\n'
                                         '1. Морс/компот, картофель фри кыстыбый Батыр\n'
                                         '\n'
                                         '2. Морс/компот, картофель фри кыстыбый Абый\n'
                                         '\n'
                                         '3. Морс/компот, картофель фри кыстыбый Кояш', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.attestation_three)
async def attestat_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти аттестацию заново')
        await call.message.answer('Аттестация провалена:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['attestation_three'] = 'ok'
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Состав ЛАНЧа №6?\n'
                                         '\n'
                                         '1. Кыстыбый Ак Барс, чай татарский 0.3, суп лапша\n'
                                         '\n'
                                         '2. Кыстыбый Абый, чай татарский 0.3, суп лапша\n'
                                         '\n'
                                         '3.', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.attestation_four)
async def attestat_four(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти аттестацию заново')
        await call.message.answer('Аттестация провалена:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['attestation_four'] = 'ok'
            await call.answer('Верно, едем дальше')
            await call.message.answer("Поздравляю, ты прошел аттестацию! Теперь ты гордость нашей команды))")
            await state.finish()


