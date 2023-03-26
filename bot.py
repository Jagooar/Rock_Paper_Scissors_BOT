from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import config


TOKEN: str = config.TOKEN

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


#@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот.\nНапиши мне что-нибудь")

#@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Напиши мне что-нибудь и в ответ "
                         "я напишу тебе твое сообщение")

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

#@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
