from aiogram import types
from keyboards.default.qoshimcha_hizmat import *
from loader import dp


@dp.message_handler(text='📩 Xalqaro SMS')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang",reply_markup=halqaro_sms_button)
@dp.message_handler(text='📩 25 xalqaro SMS')
async def bot_start(message: types.Message):
    await message.answer("""📩 25 xalqaro SMS

Yanada arzon narxlarda ko’proq SMS lar jo’nating!
5 262.5 so'm/30 kunga
Ulanish kodi: *110*041#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 50 xalqaro SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 50 xalqaro SMS

Yanada arzon narxlarda ko’proq SMS lar jo’nating!
8 420 so'm/30 kunga
Ulanish kodi: *110*042#

👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📩 100 xalqaro SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 100 xalqaro SMS

Yanada arzon narxlarda ko’proq SMS lar jo’nating!
12 630 so'm/30 kunga
Ulanish kodi: *110*043#
    
👉 @aloqa_operatorlar_bot""")