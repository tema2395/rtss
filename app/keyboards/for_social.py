from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_social_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/vahta.rtss"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Инстаграм (запрещен в РФ)", url="https://www.instagram.com/rtss_ru?igsh=MW55MjdpZ3d2OHRmNw%3D%3D&utm_source=qr"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Телеграм", url="https://t.me/GK_RT_SS"),
    )
    builder.row(
        types.InlineKeyboardButton(text="YouTube", url="https://goo.su/EnyrxK"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()