import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import adminlar
from keyboards.default.asosiy_menu import *
from loader import dp, bot,d


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.username
    try:
        d.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=asosiy_menu)
@dp.message_handler(text='🟣 Ucell')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang",reply_markup=usel_asosiy)
