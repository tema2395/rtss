import yaml
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates, FaqStates
from keyboards.for_faq import get_faq_kb
from keyboards.back import get_kb_back, get_back_and_contact_kb, get_back_and_tgcontact_kb

router = Router()


with open('text.yaml', 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)

faq_texts = yaml_data['faq']
menu_texts = yaml_data['menu']

@router.callback_query(F.data == "faq_callback")
async def faq(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Какой вопрос <b>Вас</b> интересует?", reply_markup=get_faq_kb())
    await state.set_state(MainStates.faq_state)

async def handle_question(callback: types.CallbackQuery, state: FSMContext, answer: str, next_state: FaqStates):
    await callback.message.edit_text(answer, reply_markup=get_kb_back())
    await state.set_state(next_state)

@router.callback_query(StateFilter(MainStates.faq_state))
async def handle_faq_questions(callback: types.CallbackQuery, state: FSMContext):
    question_number = int(callback.data.split('_')[1])
    if 1 <= question_number <= 15:
        answer = faq_texts['answers'][f'a{question_number}']
        next_state = getattr(FaqStates, f'q{question_number}_state')
        await handle_question(callback, state, answer, next_state)
    elif callback.data == "ques_12":
        await callback.message.edit_text(faq_texts['answers']['a12'], reply_markup=get_back_and_contact_kb())
        await state.set_state(FaqStates.q12_state)
    elif callback.data == "ques_15":
        await callback.message.edit_text(faq_texts['answers']['a15'], reply_markup=get_back_and_tgcontact_kb())
        await state.set_state(FaqStates.q15_state)

@router.callback_query(F.data == "back", StateFilter(*[getattr(FaqStates, f'q{i}_state') for i in range(1, 16)]))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await faq(callback, state)

@router.callback_query(F.data == "give_contact_callback", StateFilter(FaqStates.q12_state))
async def give_contact(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(yaml_data['support']['support_phone'], reply_markup=get_kb_back())