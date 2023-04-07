from config import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from buttons.buttons import nmts_cb
from context.context import UsersTest_1


@dp.message_handler(text='Приступить ко второму уроку.')
async def lesson2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Микроволновка')
    doc = open('/home/mekan_bot/kystbay_tgbot/kst_data/obyazsbor.docx', 'rb')
    await message.answer("Второй урок.\n"
                         "\n"
                         "Во втором уроке ты узнаешь все про зоны сборки,расстановку заказа, срок хранения, инвентарь "
                         "и как собрать доставку в наших заведениях. "
                         "Я научу тебя правильно использовать обородувания и свой мозг =)\n"
                         "Давай приступим.", reply_markup=markup)
    await message.answer("Для начала ознакомься с обязанностями сборщика. Тебе будет несложно!")
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_DOCUMENT)
    await bot.send_document(message.chat.id, document=doc)


@dp.message_handler(text='Микроволновка')
async def mircro(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чайник')
    photo = open('/home/mekan_bot/kystbay_tgbot/kst_data/micro.JPG', 'rb')
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)


@dp.message_handler(text='Чайник')
async def chay(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Бульонница')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Бульонница')
async def bul(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Кофемашина')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Кофемашина')
async def cofe(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Фритюрница')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Фритюрница')
async def free(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я ознакомился(ась), пошли дальше.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Я ознакомился(ась), пошли дальше.')
async def continue_work(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Продолжить')
    await message.answer("Пора научиться готовить продукты во фритюрнице, такие как нани, фри, наггетсы, сосиски. ",
                         reply_markup=markup)
    await message.answer('тут материалы')


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
    await message.answer('тут матриалы', reply_markup=markup)


@dp.message_handler(text='Как сделать лапшу')
async def lapsha(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать напитки: морс и компот')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как сделать напитки: морс и компот')
async def mors_compot(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как нарезать зелень, лимон')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как нарезать зелень, лимон')
async def zelen_lemon(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить сметану в соусничке')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как заполнить сметану в соусничке')
async def sous(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить витрину')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как заполнить витрину')
async def vetrina(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить пространоство расходных материалов (ложки, вилки, сахар, перец, салфетки)')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как заполнить пространоство расходных материалов (ложки, вилки, сахар, перец, салфетки)')
async def lojka_vilka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как заполнить маркет')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как заполнить маркет')
async def market(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Чистота в зоне сборки')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Чистота в зоне сборки')
async def sborka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Я усвоил(а), гоу дальше.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Я усвоил(а), гоу дальше.')
async def go(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Первые блюда: грибной крем-суп "Урман ашы", сырный суп "Кояшлы аш", "Токмач Ям", суп лапша "Токмачлы '
               'Аш".')
    await message.answer("Тебе нужно еще знать объемы стаканов, бутылок. "
                         "Ознакомиться с посудой для первых и вторых блюд, десертов и выпечки.", reply_markup=markup)
    await message.answer('тут материалы')
    await message.answer(
        '"Давай научу тебя выполнять основные действия на зоне сборки. Для начала ознакомлю тебя с составом МЕНЮ '
        '"KSTB"."')


@dp.message_handler(text='Первые блюда: грибной крем-суп "Урман ашы", сырный суп "Кояшлы аш", "Токмач Ям", суп лапша '
                         '"Токмачлы '
                         'Аш".')
async def one_blude(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Вторые блюда: балеш "Эгоист", Булгур с курицей, манты, мясо по- татарски, пельмени "Кияу".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Вторые блюда: балеш "Эгоист", Булгур с курицей, манты, мясо по- татарски, пельмени "Кияу".')
async def two_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Завтраки: завтрак 1 "Иртэ", завтрак 2 "Тан", завтрак 3 "Тэртип", завтрак 4 "Кояш", "Тост с ветчиной и '
               'сыром","сырники","каша овсяная".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(
    text='Завтраки: завтрак 1 "Иртэ", завтрак 2 "Тан", завтрак 3 "Тэртип", завтрак 4 "Кояш", "Тост с ветчиной и '
         'сыром","сырники","каша овсяная".')
async def morning_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Детское меню: "Куян Сет", кыстыбый "Бэлэкэч", детские пельмени, игрушка, сок.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Детское меню: "Куян Сет", кыстыбый "Бэлэкэч", детские пельмени, игрушка, сок.')
async def kids_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Напитки: кофе "Латте", "Капучино", "Американо", "Чай Черный", "Чай Зеленый", "морс Облепиховый", '
               'компот "Ягодный", сок 0,2.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(
    text='Напитки: кофе "Латте", "Капучино", "Американо", "Чай Черный", "Чай Зеленый", "морс Облепиховый", '
         'компот "Ягодный", сок 0,2.')
async def water_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Десерты: "Ичмасам", "Маффин", "Меренговый рулет", "Тирамису", "Чак-чак", "Чизкейк".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Десерты: "Ичмасам", "Маффин", "Меренговый рулет", "Тирамису", "Чак-чак", "Чизкейк".')
async def des_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Новинки: "салат с наггетсами","кыстыбый с пшенкой", "Пшеная каша с уткой", "суп тыквенный"')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Новинки: "салат с наггетсами","кыстыбый с пшенкой", "Пшеная каша с уткой", "суп тыквенный"')
async def new_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Салаты: салат "Уфтанма", салат "Летний".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Салаты: салат "Уфтанма", салат "Летний".')
async def salat_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('СНЭКИ: "картофель фри", "Наггетсы Чеби 3 шт", "Нани очпочмак", "Крылышки-канат".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='СНЭКИ: "картофель фри", "Наггетсы Чеби 3 шт", "Нани очпочмак", "Крылышки-канат".')
async def snek_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Выпечка: "Губадия", "Элеш", "Эчпочмак", "Балеш 1,5 кг".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Выпечка: "Губадия", "Элеш", "Эчпочмак", "Балеш 1,5 кг".')
async def belesh_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Полуфабрикаты: "Пельмени ПФ","Нани ПФ","Манты ПФ", " Наггетсы ПФ", "Сырники ПФ", "Голубцы ПФ", \n'
               '"Треуголники ПФ", "Элеши ПФ","Губадия ПФ","Балеш эгоист ПФ", "Котлеты из говядины ПФ", "Котлеты из \n'
               'курицы ПФ", "Фрикадельки говяжьи ПФ", "Фрикадельки куриные ПФ", "Тефтели ПФ".')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(
    text='Полуфабрикаты: "Пельмени ПФ","Нани ПФ","Манты ПФ", " Наггетсы ПФ", "Сырники ПФ", "Голубцы ПФ", \n'
         '"Треуголники ПФ", "Элеши ПФ","Губадия ПФ","Балеш эгоист ПФ", "Котлеты из говядины ПФ", "Котлеты из \n'
         'курицы ПФ", "Фрикадельки говяжьи ПФ", "Фрикадельки куриные ПФ", "Тефтели ПФ".')
async def fabric_blud(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Разогрев блюд')
    await message.answer('тут материалы')
    await message.answer('Молодец,дружище!\n'
                         'Теперь ты изучил полный состав меню! Если тебе нужно будет вспомнить какое-нибудь блюдо, '
                         'ты сможешь всегда воспользоваться кнопкой в меню "поиск". \n'
                         'Пора перейти к изучению Зоны Сборки.', reply_markup=markup)


@dp.message_handler(text='Разогрев блюд')
async def razogrev(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как сделать разновидности кофе')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как сделать разновидности кофе')
async def coffee_razvod(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Расстановка заказа на подносе')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Расстановка заказа на подносе')
async def rastanovka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Сборка в крафт пакете для доставки')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Сборка в крафт пакете для доставки')
async def sborka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Сборка садака')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Сборка садака')
async def sborka_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Как подписывать крышки, крафт пакеты.')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Как подписывать крышки, крафт пакеты.')
async def podpis(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Регламент по уборке кухни, зоны сборки')
    await message.answer('тут материалы', reply_markup=markup)


@dp.message_handler(text='Регламент по уборке кухни, зоны сборки')
async def reglament(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Пройти четвертый тест')
    await message.answer('тут материалы', reply_markup=markup)
    await message.answer("Поздравляю, ты прошел второй урок!.\n"
                         "Давай проверим как ты усвоил информацию.\n"
                         "Ладно, не переживай, это делается лишь для того, чтобы тебе было легче работать и кайфовать. "
                         "хихихи:)")


@dp.message_handler(text=['Пройти четвертый тест', 'Пройти четвертый тест заново'])
async def test_4(message: types.Message):
    await UsersTest_1.four_one.set()
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


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.four_one)
async def four_one(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти четвертый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '2':
        async with state.proxy() as data:
            data['four_one'] = 'ok'
            await UsersTest_1.next()
            await call.answer('Верно, едем дальше')
            await call.message.edit_text('Из чего состоит Су Анасы?\n'
                                         '\n'
                                         '1. белая лепешка, рис, соус тереяки, лосось, нори, свежий огурец\n'
                                         '2. белая лепешка, рис, соус тереяки, наггенсы, нори, корнишоны\n'
                                         '3. белая лепешка, рис, соус бургер, лосось, нори, свежий огурец',
                                         reply_markup=nmts_cb())


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.four_two)
async def four_two(call: types.CallbackQuery, state: FSMContext):
    if call.data == '2' or call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти четвертый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '1':
        async with state.proxy() as data:
            data['four_two'] = 'ok'
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


@dp.callback_query_handler(text=['1', '2', '3'], state=UsersTest_1.four_three)
async def four_three(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1' or call.data == '2':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Пройти четвертый тест заново')
        await call.message.answer('Тест провален:\n'
                                  'Все заново', reply_markup=markup)
        await state.finish()
    elif call.data == '3':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Я красавчик(ца), идем дальше.')
        async with state.proxy() as data:
            data['four_three'] = 'ok'
            await call.message.answer('Верно! едем дальше', reply_markup=markup)
            await state.finish()

