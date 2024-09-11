from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext


from bot_text.get_text import text_cfg
from keyboards.for_start import get_keyboard_menu
from states import MainStates


router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")
    
    
@router.callback_query(F.data == "back", StateFilter(MainStates.obj_info_state))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")
    
    
@router.callback_query(F.data == "back", StateFilter(MainStates.faq_state))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")
    
    
@router.callback_query(F.data == "back", StateFilter(MainStates.contacts_state))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")
    
    
    