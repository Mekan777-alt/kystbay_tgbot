from aiogram.dispatcher.filters.state import StatesGroup, State


class Users(StatesGroup):
    name = State()
    one_one = State()
    one_two = State()
    one_three = State()


