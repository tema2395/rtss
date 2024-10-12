import yaml
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.for_start import get_keyboard_menu
from states import MainStates

router = Router()

# Загрузка данных из YAML файла
with open('text.yaml', 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)

texts = yaml_data['misc']
menu_texts = yaml_data['menu']

@router.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(yaml_data["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")

@router.callback_query(F.data == "back", StateFilter(MainStates.obj_info_state, MainStates.faq_state, MainStates.contacts_state, MainStates.supp_state))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(yaml_data["hello_text"], reply_markup=get_keyboard_menu())
    await state.set_state("menu_state")