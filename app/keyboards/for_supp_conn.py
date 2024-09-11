from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_supp_conn_kb ():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Написать", url="https://t.me/rt_helpmanager"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Позвонить", callback_data="send_contact_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()