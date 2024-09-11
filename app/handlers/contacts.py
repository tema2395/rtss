from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from states import MainStates, ContactStates

from keyboards.for_contacts import get_contacts_kb
from keyboards.back import get_kb_back
from keyboards.for_social import get_social_kb
from keyboards.for_address import get_address_kb



router = Router()

@router.callback_query(F.data == "contacts_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контакты", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)
    

@router.callback_query(F.data == "number_callback", StateFilter(MainStates.contacts_state))
async def give_number(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Контактный номер: <code>+79524033544</code>", reply_markup=get_kb_back())
    await state.set_state(ContactStates.numb_state)
    
    
@router.callback_query(F.data == "back", StateFilter(ContactStates.numb_state))
async def go_back_to_contacts(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контакты", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)
    
    
@router.callback_query(F.data == "site_callback", StateFilter(MainStates.contacts_state))
async def give_site(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Сайт компании:\nhttps://rt-ss.ru", reply_markup=get_kb_back())
    await state.set_state(ContactStates.site_state)
    

@router.callback_query(F.data == "back", StateFilter(ContactStates.site_state))
async def go_back_to_contacts(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контакты", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)
    
    
@router.callback_query(F.data == "social_network_callback", StateFilter(MainStates.contacts_state))
async def give_social_contact(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши социальные сети", reply_markup=get_social_kb())
    await state.set_state(ContactStates.social_state)
    

@router.callback_query(F.data == "back", StateFilter(ContactStates.social_state))
async def go_back_to_contacts(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контакты", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)
    

@router.callback_query(F.data == "address_callback", StateFilter(MainStates.contacts_state))
async def give_address(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наш адрес:\nГ.Москва, ул.Ярославская, 10к4", reply_markup=get_address_kb())
    await state.set_state(ContactStates.address_state)
    

@router.callback_query(F.data == "back", StateFilter(ContactStates.address_state))
async def go_back_to_contacts(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Наши контакты", reply_markup=get_contacts_kb())
    await state.set_state(MainStates.contacts_state)
    
    
    
