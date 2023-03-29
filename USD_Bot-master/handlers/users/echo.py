from aiogram import types

from loader import dp,d


# Echo bot
@dp.message_handler(commands='baza')
async def bot_echo(message: types.Message):
    d.create_table_users()
    await message.answer(text='Baza yaratildi')

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
