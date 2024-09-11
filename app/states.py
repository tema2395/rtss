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
