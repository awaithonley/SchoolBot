from aiogram.dispatcher.filters.state import State, StatesGroup


class AddAdminState(StatesGroup):
    admin_id = State()
