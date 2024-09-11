from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates
from keyboards.for_objects import object_info_keyboards



router = Router()

@router.callback_query(F.data == "obj_info_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Выберите объект", reply_markup=object_info_keyboards())
    await state.set_state(MainStates.obj_info_state)
    
