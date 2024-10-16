import logging

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from states import MainStates
from keyboards.for_start import get_keyboard_menu
from bot_text.config import text_cfg  # Импорт централизованной конфигурации

router = Router()
logger = logging.getLogger(__name__)

texts = text_cfg['misc']
menu_texts = text_cfg['menu']

@router.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state(MainStates.menu_state)

@router.callback_query(F.data == "back", StateFilter(MainStates.obj_info_state, MainStates.faq_state, MainStates.contacts_state, MainStates.supp_state))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text_cfg["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state(MainStates.menu_state)
