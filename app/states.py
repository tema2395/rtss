from aiogram.fsm.state import StatesGroup, State


class MainStates(StatesGroup):
    menu_state = State()
    obj_info_state = State()
    faq_state = State()
    supp_state = State()
    contacts_state = State()
    send_contact = State()
    
    
class ContactStates(StatesGroup):
    numb_state = State()
    site_state = State()
    social_state = State()
    address_state = State()
    
    
class FaqStates(StatesGroup):
    q1_state = State()
    q2_state = State()
    q3_state = State()
    q4_state = State()
    q5_state= State()
    q6_state = State()
    q7_state = State()
    q8_state = State()
    q9_state = State()
    q10_state = State()
    q11_state = State()
    q12_state = State()
    q13_state = State()
    q14_state = State()
    q15_state = State()
