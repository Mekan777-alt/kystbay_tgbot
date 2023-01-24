from aiogram.dispatcher.filters.state import StatesGroup, State


class Users(StatesGroup):
    name = State()
    one_one = State()
    one_two = State()
    one_three = State()
    two_one = State()
    two_two = State()
    two_three = State()


