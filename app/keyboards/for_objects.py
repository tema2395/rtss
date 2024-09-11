from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def object_info_keyboards():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text='ООО "РАНТЭК-С" | Санкт-Петербург', callback_data="obj_1"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "СТРОИТЕЛЬНЫЕ СИСТЕМЫ" | Москва', callback_data="obj_2"),
    )
    builder.row(
        types.InlineKeyboardButton(text='АО "ГАЛОПОЛИМЕР ПЕРМЬ" | Пермь', callback_data="obj_3"),
    )
    builder.row(
        types.InlineKeyboardButton(text='АО "ВЗМЭО" | Волгодонск', callback_data="obj_4"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "ГАЛОПОЛИМЕР КИРОВО-ЧЕПЕЦК" | Кирово-Чепецк', callback_data="obj_5"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО «ЗНСМ» | Братск', callback_data="obj_6"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "НОВА" | Сабетта', callback_data="obj_7"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "НОВА" | Усть-Луга', callback_data="obj_8"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "ПФ "ВИС" | Салехард', callback_data="obj_9"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "ПФ "ВИС" | Якутск', callback_data="obj_10"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "РПЗ ПОЛЮС" | Хомутово', callback_data="obj_11"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "АЛЬЯНССТРОЙГАЗ" | Новокуйбышевск', callback_data="obj_12"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "АЛЬЯНССТРОЙГАЗ" | Краснодар', callback_data="obj_13"),
    )
    builder.row(
        types.InlineKeyboardButton(text='ООО "ВОЛГАДОРСТРОЙ" | Дюртюли', callback_data="obj_14")
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()
