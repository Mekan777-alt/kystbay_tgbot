from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ChatActions
from buttons.buttons import nmts_cb, nmts_cb2
from context.context import UsersTest_1
from .users_test1 import works


@dp.message_handler(text='Приступить ко второму уроку.')
async def lesson2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Микроволновка')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/obyazsbor.docx', 'rb')
    await message.answer("Второй урок.\n"
                         "\n"
                         "Во втором уроке ты узнаешь все про зоны сборки, расстановку заказа, срок хранения, инвентарь "
                         "и как собрать доставку в наших заведениях. "
                         "Я научу тебя правильно использовать обородувания и свой мозг =)\n"
                         "Давай приступим.", reply_markup=markup)
    await message.answer("Для начала ознакомься с обязанностями сборщика. Тебе будет несложно!")
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
    await bot.send_document(message.chat.id, document=doc)


@dp.message_handler(text='Микроволновка')
async def mircro(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Кофемашина')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/micro.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='Кофемашина')
async def cofe(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я ознакомился(ась), пошли дальше.')
    if works['cafe'] in '3. Спартаковская':
        file = 'BAACAgIAAxkBAAIBQGQylmOG2fb0r1GSdZHRsePFTneGAALWKwACtHKZSWdM81hyT_0jLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '1. Парина':
        file = 'BAACAgIAAxkBAAIBQGQylmOG2fb0r1GSdZHRsePFTneGAALWKwACtHKZSWdM81hyT_0jLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина':
        doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/кофемашина.pptx', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_document(message.chat.id, document=doc, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева':
        doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/кофемашина.pptx', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_document(message.chat.id, document=doc, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова':
        doc = 'BAACAgIAAxkBAAImdmRLvedk1hhUwNXiAAEcTa9ks-DdNwACQC0AApb7WUpaZNg9AAFEJ7ovBA'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Я ознакомился(ась), пошли дальше.')
async def continue_work(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Продолжить')
    file = open('/home/mekan_bot/kystbay_tgbot/kst_data/reg.pptx', 'rb')
    await message.answer("Пора научиться готовить продукты во фритюрнице, такие как нани, фри, наггетсы, сосиски. ")
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
    await bot.send_document(message.chat.id, document=file, reply_markup=markup)


@dp.message_handler(text='Продолжить')
async def con(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать заварку для чая')
    await message.answer("Прежде чем полноценно встать на зону сборки, тебе нужно научиться делать заготовки. Просто "
                         "просмотри следующую информацию, дружище))", reply_markup=markup)


@dp.message_handler(text='Как сделать заварку для чая')
async def tea(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать лапшу')
    if works['cafe'] in '3. Спартаковская':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/zavarkaspart.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    else:
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/chay.pptx', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
        await bot.send_document(message.chat.id, document=file, reply_markup=markup)


@dp.message_handler(text='Как сделать лапшу')
async def lapsha(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать напитки: морс и компот')
    file = open('/home/mekan_bot/kystbay_tgbot/kst_data/lapsha.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Как сделать напитки: морс и компот')
async def mors_compot(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как нарезать зелень, лимон')
    video = 'BAACAgIAAxkBAAIDx2Q1XfaywkjDDfUAAdx3cmUwFcJJfQACBygAAjsmsEnFuqz1AhrT0y8E'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=video, reply_markup=markup)


@dp.message_handler(text='Как нарезать зелень, лимон')
async def zelen_lemon(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить сметану в соусничке')
    file = open('/home/mekan_bot/kystbay_tgbot/kst_data/zelen.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Как заполнить сметану в соусничке')
async def sous(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить пространоство расходных материалов (ложки, вилки, сахар, перец, салфетки)')
    file = open('/home/mekan_bot/kystbay_tgbot/kst_data/smetana.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Как заполнить пространоство расходных материалов (ложки, вилки, сахар, перец, салфетки)')
async def lojka_vilka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чистота в зоне сборки')
    if works['cafe'] in '1. Парина':
        video = open('/home/mekan_bot/kystbay_tgbot/kst_data/parinarashodmat.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=video, reply_markup=markup)
    elif works['cafe'] in '3. Спартаковская':
        video = 'BAACAgIAAxkBAAIRQmRCydKwcJf6XhtifJYwRCHoGw8xAAIIMAAC4CEYStVMDvMZM9LxLwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=video, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина':
        video = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_5711.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=video, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова':
        video = 'BAACAgIAAxkBAAIRQ2RCy8XVKBgFI4IoYj5MyNjB9qFAAAIUMAAC4CEYSrXFh9PGlNM6LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=video, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева':
        video = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_8432.MP4', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=video, reply_markup=markup)


@dp.message_handler(text='Чистота в зоне сборки')
async def sborka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я усвоил(а), гоу дальше.')
    photo10 = open('/home/mekan_bot/kystbay_tgbot/kst_data/chist.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo10, reply_markup=markup)


@dp.message_handler(text='Я усвоил(а), гоу дальше.')
async def go(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Первые блюда: грибной крем-суп "Урман ашы", сырный суп "Кояшлы аш", "Токмач Ям", суп лапша "Токмачлы '
               'Аш".')
    await message.answer("Тебе нужно еще знать объемы стаканов, бутылок. "
                         "Ознакомиться с посудой для первых и вторых блюд, десертов и выпечки.", reply_markup=markup)
    file = 'BAACAgIAAxkBAAIRJWRCZZrzqR9mg7UQycDCo1mUxF2RAAKeLAAC4CEQSi6c-uOIg-ZdLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file)
    await message.answer(
        '"Давай научу тебя выполнять основные действия на зоне сборки. Для начала ознакомлю тебя с составом МЕНЮ '
        '"KSTB"."')


@dp.message_handler(text='Первые блюда: грибной крем-суп "Урман ашы", сырный суп "Кояшлы аш", "Токмач Ям", суп лапша '
                         '"Токмачлы '
                         'Аш".')
async def one_blude(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Вторые блюда: балеш "Эгоист", Булгур с курицей, манты, мясо по- татарски, пельмени "Кияу".')
    photo5 = open('/home/mekan_bot/kystbay_tgbot/kst_data/pervyybluda.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo5, reply_markup=markup)


@dp.message_handler(text='Вторые блюда: балеш "Эгоист", Булгур с курицей, манты, мясо по- татарски, пельмени "Кияу".')
async def two_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Завтраки: завтрак 1 "Иртэ", завтрак 2 "Тан", завтрак 3 "Тэртип", завтрак 4 "Кояш", "Тост с ветчиной и '
               'сыром","сырники","каша овсяная".')
    photo9 = open('/home/mekan_bot/kystbay_tgbot/kst_data/vtorybluda.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo9, reply_markup=markup)


@dp.message_handler(
    text='Завтраки: завтрак 1 "Иртэ", завтрак 2 "Тан", завтрак 3 "Тэртип", завтрак 4 "Кояш", "Тост с ветчиной и '
         'сыром","сырники","каша овсяная".')
async def morning_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Детское меню: "Куян Сет", кыстыбый "Бэлэкэч", детские пельмени, игрушка, сок.')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/zawtraki.pdf', 'rb')
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Детское меню: "Куян Сет", кыстыбый "Бэлэкэч", детские пельмени, игрушка, сок.')
async def kids_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Напитки: кофе "Латте", "Капучино", "Американо", "Чай Черный", "Чай Зеленый", "морс Облепиховый", '
               'компот "Ягодный", сок 0,2.')
    photo2 = open('/home/mekan_bot/kystbay_tgbot/kst_data/detskoye.PNG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo2, reply_markup=markup)


@dp.message_handler(
    text='Напитки: кофе "Латте", "Капучино", "Американо", "Чай Черный", "Чай Зеленый", "морс Облепиховый", '
         'компот "Ягодный", сок 0,2.')
async def water_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Десерты: "Ичмасам", "Маффин", "Меренговый рулет", "Тирамису", "Чак-чак", "Чизкейк".')
    photo4 = open('/home/mekan_bot/kystbay_tgbot/kst_data/napitki.PNG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo4, reply_markup=markup)


@dp.message_handler(text='Десерты: "Ичмасам", "Маффин", "Меренговый рулет", "Тирамису", "Чак-чак", "Чизкейк".')
async def des_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Салаты: салат "Уфтанма", салат "Летний".')
    photo7 = open('/home/mekan_bot/kystbay_tgbot/kst_data/deserty.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo7, reply_markup=markup)


@dp.message_handler(text='Салаты: салат "Уфтанма", салат "Летний".')
async def salat_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('СНЭКИ: "картофель фри", "Наггетсы Чеби 3 шт", "Нани очпочмак", "Крылышки-канат".')
    photo6 = open('/home/mekan_bot/kystbay_tgbot/kst_data/salaty.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo6, reply_markup=markup)


@dp.message_handler(text='СНЭКИ: "картофель фри", "Наггетсы Чеби 3 шт", "Нани очпочмак", "Крылышки-канат".')
async def snek_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Выпечка: "Губадия", "Элеш", "Эчпочмак", "Балеш 1,5 кг".')
    photo8 = open('/home/mekan_bot/kystbay_tgbot/kst_data/sneki.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo8, reply_markup=markup)


@dp.message_handler(text='Выпечка: "Губадия", "Элеш", "Эчпочмак", "Балеш 1,5 кг".')
async def belesh_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Полуфабрикаты: "Пельмени ПФ","Нани ПФ","Манты ПФ", " Наггетсы ПФ"')
    photo10 = open('/home/mekan_bot/kystbay_tgbot/kst_data/vypechka.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo10, reply_markup=markup)


@dp.message_handler(text='Полуфабрикаты: "Пельмени ПФ","Нани ПФ","Манты ПФ", " Наггетсы ПФ"')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 1')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/Полуфабрикаты новые цены январь.pdf', 'rb')
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 1')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 2')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/telegram.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 2')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 3')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/t2.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 3')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 4')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/t3.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 4')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 5')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/t4.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 5')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бокс 6')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/t5.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)


@dp.message_handler(text='Бокс 6')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Разогрев блюд')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/t6.mp4', 'rb')
    await bot.send_video(message.chat.id, video=doc, reply_markup=markup)
    await message.answer('Молодец, дружище!\n'
                         'Теперь ты изучил полный состав меню! Если тебе нужно будет вспомнить какое-нибудь блюдо, '
                         'ты сможешь всегда воспользоваться кнопкой в меню "поиск". \n'
                         'Пора перейти к изучению Зоны Сборки.', reply_markup=markup)


@dp.message_handler(text='Разогрев блюд')
async def razogrev(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать кофе')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/Разогрев блюд.pptx', 'rb')
    video = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_7999.MOV', 'rb')
    await bot.send_document(message.chat.id, document=doc, reply_markup=markup)
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=video, reply_markup=markup)


@dp.message_handler(text='Как сделать кофе')
async def coffee_razvod(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Расстановка заказа на подносе')
    if works['cafe'] in '3. Спартаковская':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6963.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '1. Парина':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6963.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '2. Пушкина':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6963.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '4. Ямашева':
        file = 'BAACAgIAAxkBAAImdWRLvFJ_8FrLzSgWRikclunPTDCjAAI3LQAClvtZSlO7t1aM7nE5LwQ'
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    elif works['cafe'] in '5. Кулахметова':
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/kulahkofe.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Расстановка заказа на подносе')
async def rastanovka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Сборка в крафт пакете для доставки')
    file = 'BAACAgIAAxkBAAIFkmQ2vM4nK2NagmZKjCLbE0lKtNn3AAI9KgACNCKwSRMpycu3fTxVLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Сборка в крафт пакете для доставки')
async def sborka(message: types.Message):
    if works['cafe'] != '3. Спарткавоская':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Сборка садака')
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6821.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Как подписывать крышки, крафт пакеты.')
        file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_6821.MOV', 'rb')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
        await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Сборка садака')
async def sborka_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как подписывать крышки, крафт пакеты.')
    file = open('/home/mekan_bot/kystbay_tgbot/kst_data/IMG_5750.MP4', 'rb')
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)


@dp.message_handler(text='Как подписывать крышки, крафт пакеты.')
async def podpis(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Тест по Второму уроку')
    file = 'BAACAgIAAxkBAAIDyGQ1d78lM5gsLTsFcMNVF4e8hZRpAAIDKQACOyawSdH8X58fdavfLwQ'
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_VIDEO)
    await bot.send_video(message.chat.id, video=file, reply_markup=markup)
    await message.answer("Поздравляю, ты прошел второй урок!.\n"
                         "Давай проверим как ты усвоил информацию.\n"
                         "Ладно, не переживай, это делается лишь для того, чтобы тебе было легче работать и кайфовать. "
                         "хихихи:)")


@dp.message_handler(text=['Тест по Второму уроку', 'Пройти второй тест заново'])
async def start_test_2(message: types.Message):
    await UsersTest_1.two_1.set()
    await message.answer('Сколько грамм в суп лапши входит курица и лапша?\n')


@dp.message_handler(state=UsersTest_1.two_1)
async def two_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['two_1'] = message.text
        await UsersTest_1.next()
        await message.answer('Что входит в детский набор «Куян сет»\n'
                             '\n'
                             '1. детское фри, кыстыбый «бэлэкэч», сок 0,2 либо компот, игрушка\n'
                             '\n'
                             '2. детское фри, кыстыбый «туган», сок 0,2 либо компот, игрушка\n'
                             '\n'
                             '3. детское фри, кыстыбый «бэлэкэч», сок 0,2 либо компот', reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_2)
async def two_2(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['two_2'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько по времени готовится Нани?\n'
                                         '\n'
                                         '1. 3-4 мин\n'
                                         '\n'
                                         '2. 8 мин\n'
                                         '\n'
                                         '3. 4-5 мин',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_3)
async def two_3(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        async with state.proxy() as data:
            data['two_3'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Что входит в завтрак 1 и как он называется?\n'
                                         '\n'
                                         '1. «Тан». Пюре, сосиска халяль, яичница, лепешка, зелень, лук фри, салат: '
                                         'помидоры, огурцы, айсберг, соус цезарь\n '
                                         '\n'
                                         '2. «Иртэ». Пюре, сосиска халяль, яичница, лепешка, зелень, лук фри, салат: '
                                         'помидоры, огурцы, айсберг, соус бургер\n',
                                         reply_markup=nmts_cb2())


@dp.callback_query_handler(text=['1', '2'], state=UsersTest_1.two_4)
async def two_4(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['two_4'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Что входит в состав салата «Уфтанма»?\n'
                                         '\n'
                                         '1. огурцы, болгарский перец, помидоры, айсберг, запеченная курица, '
                                         'апельсины, соус уфтанма, черный кунжут.\n '
                                         '\n'
                                         '2. огурцы, болгарский перец, айсберг, запеченная курица, апельсины, '
                                         'соус уфтанма, черный кунжут.\n '
                                         '\n'
                                         '3. огурцы, болгарский перец, айсберг, запеченная курица, апельсины, '
                                         'соус чесночный.',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_5)
async def two_5(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['two_5'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Сколько грамм по регламенту входит стандартная картошка фри и детская?\n'
                                         '\n'
                                         '1. 110 гр, 100 гр\n'
                                         '\n'
                                         '2. 100 гр, 90 гр\n'
                                         '\n'
                                         '3. 120 гр, 110 гр ',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_6)
async def two_6(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['two_6'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Cколько штук замороженых мантов входит в Полуфабрикаты? \n'
                                         '\n'
                                         '1. 7 шт\n'
                                         '\n'
                                         '2. 9 шт\n'
                                         '\n'
                                         '3. 8 шт',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.two_7)
async def two_7(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти второй тест заново')
        await call.message.answer('Давай начнем сначала))', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Я красавчик(ца), идем дальше.')
        async with state.proxy() as data:
            data['two_7'] = 'ok'
            await call.message.answer("Ты молодец, проделал(а) большую работу!\n"
                                      "Теперь ты знаешь основной состав нашего меню.\n"
                                      "Чтобы полностью усвоить зону сборки, тебе надо сделать двоеное сальто вперед ("
                                      "Латнааа татарская шутка :) ", reply_markup=markup)
            await state.finish()
