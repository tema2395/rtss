from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_faq_kb():
    builder = InlineKeyboardBuilder()
    
    builder.add(
        types.InlineKeyboardButton(text="Условия проживания?", callback_data="ques_1"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Межвахта оплачивается?", callback_data="ques_2"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Оплата сдельная или почасовая?", callback_data="ques_3"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Сколько часов длится рабочий день?", callback_data="ques_4"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Билеты вы покупаете?", callback_data="ques_5"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Билеты домой тоже покупаете вы?", callback_data="ques_6"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Мед.комиссия за чей счёт?", callback_data="ques_7"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Почему задержка заработной платы?", callback_data="ques_8"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Когда отобразится запись в электронной трудовой книжке?", callback_data="ques_9"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Где находится офис вашей компании?", callback_data="ques_10"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Есть номер бухгалтерии? кадров?", callback_data="ques_11"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Уволили или нет?", callback_data="ques_12")
    )
    builder.row(
        types.InlineKeyboardButton(text="Когда придет расчет? Можно получить расчётный лист?", callback_data="ques_13")
    )
    builder.row(
        types.InlineKeyboardButton(text="За что вычеты из заработной платы?", callback_data="ques_14")
    )
    builder.row(
        types.InlineKeyboardButton(text="Тут нет моего вопроса", callback_data="ques_15")
    )
    builder.row(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    )
    return builder.as_markup()
