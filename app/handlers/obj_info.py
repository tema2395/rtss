from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates
from keyboards.for_objects import object_info_keyboards
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_text.get_text import text_cfg

router = Router()

@router.callback_query(F.data == "obj_info_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=text_cfg["misc"]["choose_object"], reply_markup=object_info_keyboards())
    await state.set_state(MainStates.obj_info_state)

@router.callback_query(StateFilter(MainStates.obj_info_state), F.data.in_(text_cfg["object_info"].keys()))
async def show_object_info(callback: types.CallbackQuery, state: FSMContext):
    object_id = callback.data
    info = text_cfg["object_info"].get(object_id, text_cfg["misc"]["no_info"])
    
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text=text_cfg["menu"]["back"], callback_data="back_to_objects"))
    
    await callback.message.edit_text(text=info, reply_markup=builder.as_markup())

@router.callback_query(F.data == "back_to_objects")
async def back_to_objects(callback: types.CallbackQuery, state: FSMContext):
    await main_object_info(callback, state)
