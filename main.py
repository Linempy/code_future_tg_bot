from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, \
                        InlineKeyboardButton, InlineKeyboardMarkup

from config import Config


# proxy_url: str = 'http://proxy.server:3128'

bot: Bot = Bot(token=Config.BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply('Привет')


@dp.message_handler()
async def send_echo(message: Message):
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp)
