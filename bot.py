import logging
from transliterate import to_cyrillic, to_latin
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum.\nMen bilan matnlarni:\nLotin ➡️ Krill\nKrill ➡️ Lotin\nYozuvlariga o'giring. 😉\n\nAdmin: /admin")

@dp.message_handler(commands=['admin'])
async def send_welcome(message: types.Message):
    await message.reply("@Abdulaziz_Fotih")

@dp.message_handler()
async def translate(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    await message.reply(javob(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
