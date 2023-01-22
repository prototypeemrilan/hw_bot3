from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.admin_bot import log, admin,bad, ban_user, da_net


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv("BOT_TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(da_net, commands=['да'], commands_prefix=['!'])
    dp.register_message_handler(bad)

    executor.start_polling(dp, skip_updates=True)