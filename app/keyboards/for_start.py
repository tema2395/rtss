from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard_menu():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="ℹ️ Информация об объектах", callback_data="obj_info_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="📢 Частые вопросы", callback_data="faq_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="👤 Позвать специалиста", callback_data="call_supp_callback"),
    )
    builder.row(
        types.InlineKeyboardButton(text="☎️ Контактная информация", callback_data="contacts_callback"),
    )
    return builder.as_markup()
