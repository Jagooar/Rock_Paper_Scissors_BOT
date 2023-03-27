from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import config


TOKEN: str = config.TOKEN

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот.\nНапиши мне что-нибудь")

@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Напиши мне что-нибудь и в ответ "
                         "я напишу тебе твое сообщение")

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Данный вид апдейтов не поддерживается")


if __name__ == "__main__":
    dp.run_polling(bot)
