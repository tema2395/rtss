from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_address_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Как добраться?", url="https://yandex.ru/maps/213/moscow/house/yaroslavskaya_ulitsa_10k4/Z04YcANpQUIBQFtvfXRweH5hYg==/inside/?ll=37.649876%2C55.819226&tab=inside&z=17"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()