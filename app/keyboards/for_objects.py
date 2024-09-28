from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_text.get_text import text_cfg

def object_info_keyboards():
    builder = InlineKeyboardBuilder()
    
    for obj_id, obj_info in text_cfg["object_info"].items():
        obj_name = obj_info.split("\n")[0].strip()
        builder.row(types.InlineKeyboardButton(text=obj_name, callback_data=obj_id))
    
    builder.row(types.InlineKeyboardButton(text=text_cfg["menu"]["back"], callback_data="back"))
    
    return builder.as_markup()