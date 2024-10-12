import os
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from states import MainStates
from keyboards.for_objects import get_object_info_keyboard
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_text.get_text import text_cfg

router = Router()

@router.callback_query(F.data == "obj_info_callback")
async def main_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=text_cfg["misc"]["choose_object"],
        reply_markup=get_object_info_keyboard()
    )
    await state.set_state(MainStates.obj_info_state)

@router.callback_query(StateFilter(MainStates.obj_info_state), F.data.in_(text_cfg["object_info"].keys()))
async def show_object_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    object_id = callback.data
    obj_info = text_cfg["object_info"].get(object_id, {})

    if isinstance(obj_info, dict):
        name = obj_info.get("name", f"Объект {object_id}")
        description = obj_info.get("description", "Информация отсутствует")
        photo_dir = obj_info.get("photo_dir", "")
    elif isinstance(obj_info, str):
        name = obj_info.split("\n")[0].strip()
        description = obj_info
        photo_dir = ""
    else:
        await callback.message.edit_text(text=text_cfg["misc"]["no_info"])
        return

    # Подготовка медиа-группы
    media = []
    if photo_dir:
        full_photo_dir = f"photos/{photo_dir}"
        if os.path.exists(full_photo_dir):
            photo_files = [f for f in os.listdir(full_photo_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for photo in photo_files[:8]:  # Ограничиваем до 8 фото
                media.append(types.InputMediaPhoto(media=types.FSInputFile(os.path.join(full_photo_dir, photo))))

    # Если есть фотографии, отправляем их как медиа-группу
    sent_media_group = None
    if media:
        sent_media_group = await callback.message.answer_media_group(media=media)

    # Отправляем сообщение с описанием объекта и кнопкой "Назад"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text=text_cfg["menu"]["back"], callback_data="back_to_objects"))

    sent_info_message = await callback.message.answer(
        text=f"{name}\n\n{description}",
        reply_markup=builder.as_markup()
    )

    # Сохраняем сообщения для последующего удаления
    if sent_media_group:
        await state.update_data(media_group_message_ids=[message.message_id for message in sent_media_group])
    await state.update_data(info_message_id=sent_info_message.message_id)


@router.callback_query(F.data == "back_to_objects")
async def back_to_objects(callback: types.CallbackQuery, state: FSMContext):
    # Получаем данные из состояния
    data = await state.get_data()
    media_group_message_ids = data.get("media_group_message_ids", [])
    info_message_id = data.get("info_message_id")

    # Логируем полученные данные
    print(f"Media group message IDs: {media_group_message_ids}")
    print(f"Info message ID: {info_message_id}")

    # Удаляем медиагруппу, если она была и сообщения действительно существуют
    if media_group_message_ids:
        for message_id in media_group_message_ids:
            if message_id:  # Проверка, что message_id существует
                try:
                    print(f"Попытка удалить сообщение с ID: {message_id}")
                    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=message_id)
                except Exception as e:
                    print(f"Ошибка при удалении сообщения {message_id}: {e}")
            else:
                print(f"Сообщение с ID {message_id} не найдено, пропускаем удаление.")

    # Удаляем сообщение с информацией, если оно есть
    if info_message_id:
        try:
            print(f"Попытка удалить информационное сообщение с ID: {info_message_id}")
            await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=info_message_id)
        except Exception as e:
            print(f"Ошибка при удалении сообщения {info_message_id}: {e}")

    # Возвращаем меню
    await callback.message.answer(text=text_cfg["misc"]["choose_object"],
        reply_markup=get_object_info_keyboard()
    )
    await state.set_state(MainStates.obj_info_state)
