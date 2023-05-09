import smtplib
from config import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from context.context import UsersTest_1
from .users_test1 import works


async def send_mail(mail, text):
    sender = ''
    password = ''
    mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_lib.login(sender, password)
    msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
        sender, mail, 'Заявка')
    msg += text
    mail_lib.sendmail(sender, mail, msg.encode('utf8'))
    mail_lib.quit()


@dp.message_handler(text='Приступить к АТТЕСТАЦИИ.')
async def start_attestation(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать онлайн АТТЕСТАЦИЮ')
    await message.answer("Вот и настало время Аттестации. Будь спокоен, ведь всю важную информацию ты уже усвоил. "
                         "Повтори то, что ты плохо запомнил. Теперь выдохни!)) Ты усвоил столько навыков в "
                         "сети-ресторанов 'KSTB', я тебя поздравляю!!! После прохождения онлайн-аттестации сообщи об "
                         "этом своему руководителю.", reply_markup=markup)


@dp.message_handler(text='Приступить к АТТЕСТАЦИИ.')
async def start_attestation(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Начать онлайн АТТЕСТАЦИЮ')
    await message.answer("Вот и настало время Аттестации. Будь спокоен, ведь всю важную информацию ты уже усвоил. "
                         "Повтори то, что ты плохо запомнил. Теперь выдохни!)) Ты усвоил столько навыков в "
                         "сети-ресторанов 'KSTB', я тебя поздравляю!!! После прохождения онлайн-аттестации сообщи об "
                         "этом своему руководителю.\n"
                         "\n"
                         "«Дорогой друг, во время ответа на вопросы, постарайся дать развернутые ответы»",
                         reply_markup=markup)


@dp.message_handler(text='Начать онлайн АТТЕСТАЦИЮ')
async def st_att(message: types.Message):
    await UsersTest_1.attestation_1.set()
    await message.answer('Напиши состав Кыстыбый Алтын, Су Анасы')


@dp.message_handler(state=UsersTest_1.attestation_1)
async def att_1(message: types.Message):
    works['attestation_1'] = message.text
    await UsersTest_1.next()
    await message.answer('Какая миссия компании КСТБ?')


@dp.message_handler(state=UsersTest_1.attestation_2)
async def att_2(message: types.Message):
    works['attestation_2'] = message.text
    await UsersTest_1.next()
    await message.answer('Что входит в Комбо №3?')


@dp.message_handler(state=UsersTest_1.attestation_3)
async def att_3(message: types.Message):
    works['attestation_3'] = message.text
    await UsersTest_1.next()
    await message.answer('Что такое губадия? эчпочмак?')


@dp.message_handler(state=UsersTest_1.attestation_4)
async def att_4(message: types.Message):
    works['attestation_4'] = message.text
    await UsersTest_1.next()
    await message.answer('Завтрак 1? Название, состав')


@dp.message_handler(state=UsersTest_1.attestation_5)
async def att_6(message: types.Message):
    works['attestation_5'] = message.text
    await UsersTest_1.next()
    await message.answer('Добавка доп сыр – сколько порции?')


@dp.message_handler(state=UsersTest_1.attestation_6)
async def att_7(message: types.Message):
    works['attestation_6'] = message.text
    await UsersTest_1.next()
    await message.answer('Как подают Кояшлы аш')


@dp.message_handler(state=UsersTest_1.attestation_7)
async def att_8(message: types.Message):
    works['attestation_7'] = message.text
    await UsersTest_1.next()
    await message.answer('Зашел гость, последовательность обслуживания?')


@dp.message_handler(state=UsersTest_1.attestation_8)
async def att_9(message: types.Message):
    works['attestation_8'] = message.text
    await UsersTest_1.next()
    await message.answer('Как мы работаем с конфликтными ситуациями?')


@dp.message_handler(state=UsersTest_1.attestation_9)
async def att_10(message: types.Message):
    works['attestation_9'] = message.text
    await UsersTest_1.next()
    await message.answer('Ты на сборке, гость просит убрать стол?')


@dp.message_handler(state=UsersTest_1.attestation_10)
async def att_11(message: types.Message):
    works['attestation_10'] = message.text
    await UsersTest_1.next()
    await message.answer('Какие вторичные обязанности у кассира?')


@dp.message_handler(state=UsersTest_1.attestation_11)
async def att_12(message: types.Message):
    works['attestation_11'] = message.text
    await UsersTest_1.next()
    await message.answer('Гость заказал Ланч №2, чизкейк, манты. Какая будет расстановка на подносе?')


@dp.message_handler(state=UsersTest_1.attestation_12)
async def att_13(message: types.Message):
    works['attestation_12'] = message.text
    await UsersTest_1.next()
    await message.answer('Гость спрашивает, что в составе Булгура с курицей?')


@dp.message_handler(state=UsersTest_1.attestation_13)
async def att_14(message: types.Message):
    works['attestation_13'] = message.text
    await UsersTest_1.next()
    await message.answer('У гостя в заказе Комбо №5, булгур, уфтанма, капучино – последовательность сборки?')


@dp.message_handler(state=UsersTest_1.attestation_14)
async def att_15(message: types.Message):
    works['attestation_14'] = message.text
    await UsersTest_1.next()
    await message.answer('Сколько мл сгущенки наливается в соусничку?')


@dp.message_handler(state=UsersTest_1.attestation_15)
async def att_16(message: types.Message):
    works['attestation_15'] = message.text
    await UsersTest_1.next()
    await message.answer('Состав супа Токмач Ям?')


@dp.message_handler(state=UsersTest_1.attestation_16)
async def att_17(message: types.Message):
    works['attestation_16'] = message.text
    await UsersTest_1.next()
    await message.answer('Как собираем с собой доставку Ланч 2, Уфтанма?')


@dp.message_handler(state=UsersTest_1.attestation_17)
async def att_18(message: types.Message):
    works['attestation_17'] = message.text
    await UsersTest_1.next()
    await message.answer('Как часто проверяем (чистим) санузлы?')


@dp.message_handler(state=UsersTest_1.attestation_18)
async def att_19(message: types.Message):
    works['attestation_18'] = message.text
    await UsersTest_1.next()
    await message.answer('Как происходит закрытие смены?')


@dp.message_handler(state=UsersTest_1.attestation_19)
async def att_20(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardRemove()
    works['attestation_19'] = message.text
    works.clear()
    await message.answer('"Поздравляю, ты прошел аттестацию! Теперь ты гордость нашей команды))"',
                         reply_markup=markup)
    await state.finish()
