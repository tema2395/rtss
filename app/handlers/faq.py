import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from states import MainStates, FaqStates
from keyboards.for_faq import get_faq_kb
from keyboards.back import get_kb_back, get_back_and_contact_kb, get_back_and_tgcontact_kb
from bot_text.config import text_cfg  # Импорт централизованной конфигурации

router = Router()
logger = logging.getLogger(__name__)

faq_texts = text_cfg['faq']
menu_texts = text_cfg['menu']

@router.callback_query(F.data == "faq_callback")
async def faq(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Какой вопрос <b>Вас</b> интересует?", reply_markup=get_faq_kb())
    await state.set_state(MainStates.faq_state)

async def handle_question(callback: types.CallbackQuery, state: FSMContext, answer: str, next_state: FaqStates):
    await callback.message.edit_text(answer, reply_markup=get_kb_back())
    await state.set_state(next_state)

@router.callback_query(StateFilter(MainStates.faq_state))
async def handle_faq_questions(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data
    if data.startswith("ques_"):
        question_number = data.split('_')[1]
        if question_number.isdigit():
            question_number = int(question_number)
            if 1 <= question_number <= 15:
                answer = faq_texts['answers'].get(f'a{question_number}', "Ответ не найден.")
                state_attr = f'q{question_number}_state'
                next_state = getattr(FaqStates, state_attr, None)
                if next_state:
                    if data in ["ques_12", "ques_15"]:
                        if data == "ques_12":
                            await callback.message.edit_text(faq_texts['answers']['a12'], reply_markup=get_back_and_contact_kb())
                            await state.set_state(FaqStates.q12_state)
                        elif data == "ques_15":
                            await callback.message.edit_text(faq_texts['answers']['a15'], reply_markup=get_back_and_tgcontact_kb())
                            await state.set_state(FaqStates.q15_state)
                    else:
                        await handle_question(callback, state, answer, next_state)
                else:
                    logger.warning(f"Неизвестное состояние для вопроса {question_number}")
            else:
                logger.warning(f"Номер вопроса {question_number} вне диапазона.")
        else:
            logger.warning(f"Неверный формат номера вопроса: {question_number}")
    else:
        logger.warning(f"Неизвестный формат данных: {data}")

@router.callback_query(F.data == "back", StateFilter(*[getattr(FaqStates, f'q{i}_state') for i in range(1, 16)]))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await faq(callback, state)

@router.callback_query(F.data == "give_contact_callback", StateFilter(FaqStates.q12_state))
async def give_contact(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text_cfg['support']['support_phone'], reply_markup=get_kb_back())
