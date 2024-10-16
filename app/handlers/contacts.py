import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from states import MainStates, ContactStates
from keyboards.for_contacts import get_contacts_kb
from keyboards.back import get_kb_back
from keyboards.for_social import get_social_kb
from keyboards.for_address import get_address_kb
from bot_text.config import text_cfg  # Импорт централизованной конфигурации

router = Router()
logger = logging.getLogger(__name__)

contacts_texts = text_cfg['contacts']
menu_texts = text_cfg['menu']

@router.callback_query(F.data == "contacts_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контактные данные", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)

@router.callback_query(F.data == "number_callback", StateFilter(MainStates.contacts_state))
async def give_number(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(contacts_texts['phone'], reply_markup=get_kb_back())
    await state.set_state(ContactStates.numb_state)

@router.callback_query(F.data == "site_callback", StateFilter(MainStates.contacts_state))
async def give_site(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=contacts_texts['site'], reply_markup=get_kb_back())
    await state.set_state(ContactStates.site_state)

@router.callback_query(F.data == "social_network_callback", StateFilter(MainStates.contacts_state))
async def give_social_contact(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=contacts_texts['social_networks'], reply_markup=get_social_kb())
    await state.set_state(ContactStates.social_state)

@router.callback_query(F.data == "address_callback", StateFilter(MainStates.contacts_state))
async def give_address(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=contacts_texts['address'], reply_markup=get_address_kb())
    await state.set_state(ContactStates.address_state)

@router.callback_query(F.data == "back", StateFilter(ContactStates.numb_state, ContactStates.site_state, ContactStates.social_state, ContactStates.address_state))
async def go_back_to_contacts(callback: types.CallbackQuery, state: FSMContext):
    await main_object_info(callback, state)
