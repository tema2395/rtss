import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import start, obj_info, faq, contacts, call_supp

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

bot = Bot(
    os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(obj_info.router)
dp.include_router(faq.router)
dp.include_router(contacts.router)
dp.include_router(call_supp.router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Бот запущен и начал опрос обновлений.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
