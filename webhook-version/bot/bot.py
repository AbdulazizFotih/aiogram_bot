import logging
from .transliterate import to_cyrillic, to_latin
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from bot.settings import (BOT_TOKEN, HEROKU_APP_NAME,
                          WEBHOOK_URL, WEBHOOK_PATH,
                          WEBAPP_HOST, WEBAPP_PORT)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# @dp.message_handler()
# async def echo(message: types.Message):
#     logging.warning(f'Recieved a message from {message.from_user}')
#     await bot.send_message(message.chat.id, message.text)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    logging.warning(f'Recieved a message from {message.from_user}')
    await message.reply("Assalomu alaykum.\nMen bilan matnlarni:\nLotin ➡️ Krill\nKrill ➡️ Lotin\nYozuvlariga o'giring. 😉\n\nAdmin: /admin")

@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    await message.reply("@Abdulaziz_Fotih")

@dp.message_handler()
async def translate(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    await message.reply(javob(msg))


async def on_startup(dp):
    logging.warning(
        'Starting connection. ')
    await bot.set_webhook(WEBHOOK_URL,drop_pending_updates=True)


async def on_shutdown(dp):
    logging.warning('Bye! Shutting down webhook connection')


def main():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
