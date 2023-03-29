from aiogram import types

from keyboards.default.asosiy_menu import *
from keyboards.default.tariflar import *
from loader import dp


@dp.message_handler(text='🟡 Beeline')
async def bot_start(message: types.Message):
    await message.answer(f"Xizmatlarni tanlashingiz mumkin",reply_markup=asosiy_ichi)
@dp.message_handler(text='📔 Tariflar')
async def bot_start(message: types.Message):
    await message.answer(f"Tariflarni tanlashingiz mumkin",reply_markup=tariflar_button)

@dp.message_handler(text='🏠 Bosh menu')
async def bot_start(message: types.Message):
    await message.answer(f"Asosiy menu",reply_markup=asosiy_menu)

@dp.message_handler(text='<-Orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Ortga qaytdingiz",reply_markup=asosiy_menu)
@dp.message_handler(text='🌏 Internet')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang",reply_markup=internet_button)
@dp.message_handler(text='<- Orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Ortga qaytdingiz",reply_markup=asosiy_ichi)
@dp.message_handler(text='📁 Boshqa hizmatlar')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang",reply_markup=boshqa_hizmatlar_button)
