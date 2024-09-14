from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates, FaqStates
from keyboards.for_faq import get_faq_kb
from keyboards.back import get_kb_back, get_back_and_contact_kb, get_back_and_tgcontact_kb


router = Router()

@router.callback_query(F.data == "faq_callback")
async def faq(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Какой вопрос <b>Вас</b> интересует?", reply_markup=get_faq_kb())
    await state.set_state(MainStates.faq_state)

async def handle_question(callback: types.CallbackQuery, state: FSMContext, answer: str, next_state: FaqStates):
    await callback.message.edit_text(answer, reply_markup=get_kb_back())
    await state.set_state(next_state)

@router.callback_query(StateFilter(MainStates.faq_state))
async def handle_faq_questions(callback: types.CallbackQuery, state: FSMContext):
    question_answers = {
        "ques_1": ("Комфортабельное общежитие / квартира / хостел", FaqStates.q1_state),
        "ques_2": ("Нет, но выплачивается премия после возвращения с межвахты в размере 7000 руб.", FaqStates.q2_state),
        "ques_3": ("Почасовая.", FaqStates.q3_state),
        "ques_4": ("На каждом объекте по-разному, в среднем с 8:00 до 19:00", FaqStates.q4_state),
        "ques_5": ("Да, билеты приобретаются за счет организации", FaqStates.q5_state),
        "ques_6": ("Да, билеты приобретаются за счет организации", FaqStates.q6_state),
        "ques_7": ("Мед. комиссию оплачивает организация", FaqStates.q7_state),
        "ques_8": ("Из-за банковской системы. Срок зачисления денежных средств на счет составляет 3 рабочих дня. Если задержка дольше, обратитесь к оператору за более подробной информацией", FaqStates.q8_state),
        "ques_9": ("Примерно через 3 рабочих дня с момента трудоустройства", FaqStates.q9_state),
        "ques_10": ("Наш головной офис находится в г. Москва. Также имеются представительства в других регионах", FaqStates.q10_state),
        "ques_11": ("Вся интересующая Вас информация отображена здесь, если Вы не нашли ответ на свой вопрос, свяжитесь с оператором", FaqStates.q11_state),
        "ques_13": ("Расчётный лист Вам высылает ваш менеджер в течение трёх рабочих дней после поступления основной заработной платы, если Вы не нашли ответ на свой вопрос, свяжитесь с оператором", FaqStates.q13_state),
        "ques_14": ("Все вычеты, кроме НДФЛ, осуществляются вручную производственным отделом. Для более подробной информации Вы можете связаться с оператором", FaqStates.q14_state),
    }
    
    if callback.data in question_answers:
        await handle_question(callback, state, *question_answers[callback.data])
    elif callback.data == "ques_12":
        await callback.message.edit_text("Для более подробной информации, свяжитесь с оператором", reply_markup=get_back_and_contact_kb())
        await state.set_state(FaqStates.q12_state)
    elif callback.data == "ques_15":
        await callback.message.edit_text("Для более подробной информации, свяжитесь с оператором", reply_markup=get_back_and_tgcontact_kb())
        await state.set_state(FaqStates.q15_state)


@router.callback_query(F.data == "back", StateFilter(*[getattr(FaqStates, f"q{i}_state") for i in range(1, 16)]))
async def back_to_menu(callback: types.CallbackQuery, state: FSMContext):
    await faq(callback, state)

@router.callback_query(F.data == "give_contact_callback", StateFilter(FaqStates.q12_state))
async def give_contact(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Телефон технической поддержки:\n\n<code>+7 922 686-96-18</code>", reply_markup=get_kb_back())

@router.callback_query(F.data == "back", StateFilter(FaqStates.q12_state))
async def back_to_menu_from_contact(callback: types.CallbackQuery, state: FSMContext):
    await faq(callback, state)
