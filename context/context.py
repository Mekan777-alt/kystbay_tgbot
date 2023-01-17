from aiogram.dispatcher.filters.state import StatesGroup, State


class Users(StatesGroup):
    name = State()
    street = State()
    video_1 = State()
    video_2 = State()
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()

