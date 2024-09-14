from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb_back():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back"),
    )
    return builder.as_markup()


def get_back_and_contact_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Связаться с оператором", callback_data="give_contact_callback")
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()


def get_back_and_tgcontact_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Связаться с оператором", url="https://t.me/rt_helpmanager")
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()