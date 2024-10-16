import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states import MainStates
from keyboards.for_objects import get_object_info_keyboard
from keyboards.back import get_kb_back
from bot_text.config import text_cfg  # Импорт централизованной конфигурации

router = Router()
logger = logging.getLogger(__name__)

@router.callback_query(F.data == "obj_info_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    # Удаляем текущее меню объектов
    await callback.message.delete()

    # Отправляем меню объектов снова
    sent_menu_message = await callback.message.answer(
        text=text_cfg["misc"]["choose_object"],
        reply_markup=get_object_info_keyboard()
    )
    await state.set_state(MainStates.obj_info_state)

    # Сохраняем message_id меню для возможного удаления (опционально)
    await state.update_data(menu_message_id=sent_menu_message.message_id)

@router.callback_query(StateFilter(MainStates.obj_info_state), F.data.in_(text_cfg["object_info"].keys()))
async def show_object_info(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    previous_media_group_message_ids = data.get("media_group_message_ids", [])
    previous_info_message_id = data.get("info_message_id")
    menu_message_id = data.get("menu_message_id")

    # Удаляем предыдущие сообщения с фотографиями, если они есть
    for message_id in previous_media_group_message_ids:
        try:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении медиа-сообщения {message_id}: {e}")

    # Удаляем предыдущее информационное сообщение, если оно есть
    if previous_info_message_id:
        try:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=previous_info_message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении информационного сообщения {previous_info_message_id}: {e}")

    # Удаляем меню объектов, если оно сохранялось
    if menu_message_id:
        try:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=menu_message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении меню объектов {menu_message_id}: {e}")

    # Получаем информацию об объекте
    object_id = callback.data
    obj_info = text_cfg["object_info"].get(object_id, {})

    if not obj_info:
        await callback.message.answer(text=text_cfg["misc"]["no_info"])
        return

    name = obj_info.get("name", f"Объект {object_id}")
    description = obj_info.get("description", "Информация отсутствует")
    photo_urls = obj_info.get("photos", [])

    # Инициализируем список для сохранения message_id медиа-сообщений
    media_group_message_ids = []

    # Отправляем медиа-группу, если есть фотографии
    if photo_urls:
        media = [
            types.InputMediaPhoto(media=url)
            for url in photo_urls[:10]  # Ограничиваем до 10 фото
        ]

        try:
            sent_media_group = await callback.message.answer_media_group(media=media)
            media_group_message_ids = [message.message_id for message in sent_media_group]
        except Exception as e:
            logger.error(f"Ошибка при отправке медиа-группы: {e}")
            await callback.message.answer("Не удалось загрузить фотографии. Пожалуйста, попробуйте позже.")

    # Отправляем сообщение с информацией об объекте и кнопкой "Назад"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text=text_cfg["menu"]["back"], callback_data="back_to_objects"))

    try:
        sent_info_message = await callback.message.answer(
            text=f"{name}\n\n{description}",
            reply_markup=builder.as_markup()
        )
        info_message_id = sent_info_message.message_id
    except Exception as e:
        logger.error(f"Ошибка при отправке информационного сообщения: {e}")
        info_message_id = None

    # Сохраняем message_id для последующего удаления
    await state.update_data(media_group_message_ids=media_group_message_ids, info_message_id=info_message_id)

@router.callback_query(F.data == "back_to_objects", StateFilter(MainStates.obj_info_state))
async def back_to_objects(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    media_group_message_ids = data.get("media_group_message_ids", [])
    info_message_id = data.get("info_message_id")
    menu_message_id = data.get("menu_message_id")

    # Удаляем медиа-группу, если она была
    for message_id in media_group_message_ids:
        try:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении медиа-сообщения {message_id}: {e}")

    # Удаляем информационное сообщение, если оно было
    if info_message_id:
        try:
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=info_message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении информационного сообщения {info_message_id}: {e}")

    # Отправляем меню объектов снова
    sent_menu_message = await callback.message.answer(
        text=text_cfg["misc"]["choose_object"],
        reply_markup=get_object_info_keyboard()
    )

    # Обновляем состояние, сохраняя новое menu_message_id и очищая предыдущие
    await state.update_data(
        media_group_message_ids=[],
        info_message_id=None,
        menu_message_id=sent_menu_message.message_id
    )
