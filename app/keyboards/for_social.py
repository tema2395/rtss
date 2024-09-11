from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_social_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Номер телефона", callback_data="number_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Сайт компании", callback_data="site_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Социальные сети", callback_data="social_network_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Адрес", callback_data="address"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()