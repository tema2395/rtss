from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates
from keyboards.for_faq import get_faq_kb


router = Router()

@router.callback_query(F.data == "faq_callback")
async def faq(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Какой вопрос <b>Вас</b> интересует?", reply_markup=get_faq_kb())
    await state.set_state(MainStates.faq_state)