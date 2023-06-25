import smtplib
from config import dp, db_link
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from context.context import UsersTest_1
from .users_test1 import works
import sqlite3


async def send_mail(mail, text):
    sender = 'kstbhr@yandex.ru'
    password = 'kstb1986!'
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
async def att_1(message: types.Message, state: FSMContext):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_1=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Какая миссия компании КСТБ?')


@dp.message_handler(state=UsersTest_1.attestation_2)
async def att_2(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_2=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Что входит в Комбо №3?')


@dp.message_handler(state=UsersTest_1.attestation_3)
async def att_3(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_3=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Что такое губадия? эчпочмак?')


@dp.message_handler(state=UsersTest_1.attestation_4)
async def att_4(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_4=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Завтрак 1? Название, состав')


@dp.message_handler(state=UsersTest_1.attestation_5)
async def att_6(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_5=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Добавка доп сыр – сколько порции?')


@dp.message_handler(state=UsersTest_1.attestation_6)
async def att_7(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_6=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Как подают Кояшлы аш')


@dp.message_handler(state=UsersTest_1.attestation_7)
async def att_8(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_7=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Зашел гость, последовательность обслуживания?')


@dp.message_handler(state=UsersTest_1.attestation_8)
async def att_9(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_8=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Как мы работаем с конфликтными ситуациями?')


@dp.message_handler(state=UsersTest_1.attestation_9)
async def att_10(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_9=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Ты на сборке, гость просит убрать стол?')


@dp.message_handler(state=UsersTest_1.attestation_10)
async def att_11(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_10=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Какие вторичные обязанности у кассира?')


@dp.message_handler(state=UsersTest_1.attestation_11)
async def att_12(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_11=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Гость заказал Ланч №2, чизкейк, манты. Какая будет расстановка на подносе?')


@dp.message_handler(state=UsersTest_1.attestation_12)
async def att_13(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_12=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Гость спрашивает, что в составе Булгура с курицей?')


@dp.message_handler(state=UsersTest_1.attestation_13)
async def att_14(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_13=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('У гостя в заказе Комбо №5, булгур, уфтанма, капучино – последовательность сборки?')


@dp.message_handler(state=UsersTest_1.attestation_14)
async def att_15(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_14=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Сколько мл сгущенки наливается в соусничку?')


@dp.message_handler(state=UsersTest_1.attestation_15)
async def att_16(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_15=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Состав супа Токмач Ям?')


@dp.message_handler(state=UsersTest_1.attestation_16)
async def att_17(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_16=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Как собираем с собой доставку Ланч 2, Уфтанма?')


@dp.message_handler(state=UsersTest_1.attestation_17)
async def att_18(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_17=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Как часто проверяем (чистим) санузлы?')


@dp.message_handler(state=UsersTest_1.attestation_18)
async def att_19(message: types.Message):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_18=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    conn.close()
    await UsersTest_1.next()
    await message.answer('Как происходит закрытие смены?')


@dp.message_handler(state=UsersTest_1.attestation_19)
async def att_20(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardRemove()
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET at_19=? WHERE chat_id=?", (str(message.text), message.chat.id))
    conn.commit()
    data = cursor.execute("SELECT * FROM users WHERE chat_id = ?", (message.chat.id, )).fetchall()
    for row in data:
        all_info = f"Имя {row[2]}\n" \
               f"Точка {row[3]}\n" \
               f"______________________\n" \
               f"2 тест 1 ответ {row[4]}\n" \
               f"_________________________________\n" \
               f"Аттестация:\n" \
               f"1. {row[5]}\n" \
               f"2. {row[6]}\n" \
               f"3. {row[7]}\n" \
               f"4. {row[8]}\n" \
               f"5. {row[9]}\n" \
               f"6. {row[10]}\n" \
               f"7. {row[11]}\n" \
               f"8. {row[12]}\n" \
               f"9. {row[13]}\n" \
               f"10. {row[14]}\n" \
               f"11. {row[15]}\n" \
               f"12. {row[16]}\n" \
               f"13. {row[17]}\n" \
               f"14. {row[18]}\n" \
               f"15. {row[19]}\n" \
               f"16. {row[20]}\n" \
               f"17. {row[21]}\n" \
               f"18. {row[22]}\n" \
               f"19. {row[23]}\n"
        await send_mail('HRtest@kstb.cafe', all_info)
    await message.answer('"Поздравляю, ты прошел аттестацию! Теперь ты гордость нашей команды))"',
                         reply_markup=markup)
    await state.finish()
