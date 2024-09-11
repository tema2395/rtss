from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def object_info_keyboards():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="Объект 1", callback_data="obj_1"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Объект 2", callback_data="obj_2"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Объект 3", callback_data="obj_3"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Объект 4", callback_data="obj_4"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()
