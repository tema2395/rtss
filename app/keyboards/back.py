from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb_back():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back"),
    )
    return builder.as_markup()