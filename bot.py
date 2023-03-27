import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

import config


TOKEN: str = config.TOKEN

# Объекты бота и диспетчера
bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()

# Кол-во попыток в игре
ATTEMPTS: int = 5

# Словарь с данными пользователя
user: dict = {'in_game': False,
              "secret_number": None,
              'attempts': None,
              'total_game': 0,
              'wins': 0}

# Функция возврата случайного целого числа
def get_random_number() -> int:
    return random.randint(1, 100)

# Хэндлер обработки команды start
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\n'
                         'Давай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список команд - '
                         'отправь команду /help')

# Хэндлер обработки команды help
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры: '
                         f'Я загадываю число от 1 до 100, '
                         f'а тебе нужно его угадать за {ATTEMPTS} попыток\n'
                         f'Каманды: '
                         f'/help - правила игры и список команд, '
                         f'/сancel - выйти из игры, /stat - статистика\n\n'
                         f'Давай сыграем?')

# Хэндлер обработки команды stat
@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_game"]}\n'
                         f'Игр выиграно: {user["wins"]}')

# Хэндлер обработки команды cansel
@dp.message(Command(commands=['cancel']))
async def process_cansel_command(message: Message):
    if user['in_game']:
        await  message.answer('Игра завершена')
        user['in_game'] = False
    else:
        await message.answer('Игра не начата')

# Хендлер обработки согласия сыграть в игру
@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть'],
                       ignore_case=True))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Здорово!\n'
                             'Я загадал число от 1 до 100, '
                             'попробуй угадать')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Идет игра, я могу реагировать только на числа '
                             'от 1 до 100 и команды /cansel и /help')

# Хэндлер обработки отказа сыграть в игру
@dp.message(Text(text=['Нет', 'Не', 'Не хочу'], ignore_case=True))
async def process_negativ_answer(message: Message):
    if not user['in_game']:
        await message.answer('Очень жаль:(')
    else:
        await message.answer('Идет игра. Присылай числа от 1 до 100')

# Хэндлер обработки отправленных чисел
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура! Вы угадали!\nСыграем ещё?')
            user['in_game'] = False
            user['total_game'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Загаданное число меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Загаданное число больше')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'Больше не осталось попыток. Ты проиграл.\n'
                                f'Я загадывал число {user["secret_number"]}\n'
                                f'Сыграем ещё?')
            user['in_game'] = False
            user['total_game'] += 1
    else:
        await message.answer('Мы еще не играем. Начнем игру?')

# Хэндлер обработки всех остальных сообщений
@dp.message()
async def process_other_text(message: Message):
    if user['in_game']:
        await message.answer('Начата игра, жду чисел от 1 до 100')
    else:
        await message.answer('Не знаю что на это ответить')


if __name__ == '__main__':
    dp.run_polling(bot)