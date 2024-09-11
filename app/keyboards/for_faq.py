from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_faq_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Вопрос 1", callback_data="ques_1"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Вопрос 2", callback_data="ques_2"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Вопрос 3", callback_data="ques_3"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Вопрос 4", callback_data="ques_4"),
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()
