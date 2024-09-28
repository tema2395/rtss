from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from keyboards.for_supp_conn import get_supp_conn_kb
from keyboards.back import get_kb_back
from states import MainStates

router = Router()

@router.callback_query(F.data == "call_supp_callback")
async def give_contact_supp(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Выберите, как <b>Вам</b> удобно связаться с нами", reply_markup=get_supp_conn_kb())
    await state.set_state(MainStates.supp_state)
    
@router.callback_query(F.data == "send_contact_callback")
async def give_number(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Телефон технической поддержки:\n\n<code>+7 922 686-96-18</code>", reply_markup=get_kb_back())
    await state.set_state(MainStates.send_contact)
    
    
@router.callback_query(F.data == "back", StateFilter(MainStates.send_contact))
async def get_back_to_call_sup(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Выберите, как <b>Вам</b> удобно связаться с нами", reply_markup=get_supp_conn_kb())
    await state.set_state(MainStates.supp_state)
            




