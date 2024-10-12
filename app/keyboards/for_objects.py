from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_text.get_text import text_cfg

def get_object_info_keyboard():
    builder = InlineKeyboardBuilder()
    for obj_id, obj_info in text_cfg["object_info"].items():
        if isinstance(obj_info, dict) and "name" in obj_info:
            obj_name = obj_info["name"]
        elif isinstance(obj_info, str):
            obj_name = obj_info.split("\n")[0].strip()
        else:
            obj_name = f"Объект {obj_id}"
        builder.row(types.InlineKeyboardButton(text=obj_name, callback_data=obj_id))
    builder.row(types.InlineKeyboardButton(text=text_cfg["menu"]["back"], callback_data="back"))
    return builder.as_markup()