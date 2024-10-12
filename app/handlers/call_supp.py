import yaml
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from keyboards.for_supp_conn import get_supp_conn_kb
from keyboards.back import get_kb_back
from states import MainStates

router = Router()

# Загрузка данных из YAML файла
with open('text.yaml', 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)

support_texts = yaml_data['support']
menu_texts = yaml_data['menu']

@router.callback_query(F.data == "call_supp_callback")
async def give_contact_supp(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(support_texts['choose_contact_method'], reply_markup=get_supp_conn_kb())
    await state.set_state(MainStates.supp_state)

@router.callback_query(F.data == "send_contact_callback")
async def give_number(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(support_texts['support_phone'], reply_markup=get_kb_back())
    await state.set_state(MainStates.send_contact)

@router.callback_query(F.data == "back", StateFilter(MainStates.send_contact))
async def get_back_to_call_sup(callback: types.CallbackQuery, state: FSMContext):
    await give_contact_supp(callback, state)