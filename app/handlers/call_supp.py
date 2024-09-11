from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from keyboards.for_supp_conn import get_supp_conn_kb
from states import MainStates

router = Router()

@router.callback_query(F.data == "call_supp_callback")
async def give_contact_supp(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Выберите, как <b>Вам</b> удобно связаться с нами", reply_markup=get_supp_conn_kb())
    await state.set_state(MainStates.supp_state)
    
@router.callback_query(F.data == "send_contact_callback")
async def give_number(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer_contact(phone_number="+79226869618", first_name="Служба Поддержки")
    



