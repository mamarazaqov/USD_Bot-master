from aiogram import types
from keyboards.default.qoshimcha_hizmat import *

from loader import dp


@dp.message_handler(text='📩 SMS xizmatlar')
async def bot_help(message: types.Message):
    await message.answer(text='📩 SMS xizmatlar',reply_markup=sms_button)
@dp.message_handler(text='📨 20 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 20 SMS paketi

500 so'm/kun
Ulanish narxi 0 so'm
Ulanish uchun hisobdagi minimal mablag’ miqdori 600 so'm
Ulanish kodi: *110*161#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 50 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 50 SMS paketi

1 000 so'm/kun
Ulanish narxi 0 so'm
Ulanish uchun hisobdagi minimal mablag' miqdori 1 100 so'm
Ulanish kodi: *110*162#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 SMS non-stop')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 SMS non-stop

«SMS non-stop» xizmati bilan siz kuniga 250 ta mahalliy SMS olasiz. 
1 300 so'm/kun
Ulanish kodi: *110*151#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 100 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 100 SMS paketi 
Yanada ko’proq SMS muloqot!
5 262.5 so'm/30 kunga
Ulanish kodi: *110*044#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 500 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 500 SMS paketi

Yanada ko’proq SMS muloqot!
13 682.5 so'm/30 kunga
Ulanish kodi: *110*045#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 1000 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""📨 1000 SMS paketi 

Yanada ko’proq SMS muloqot!
22 102.5 so'm/30 kunga
Ulanish kodi: *110*046#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📸 SMS Flash')
async def bot_help(message: types.Message):
    await message.answer(text="""📸 SMS Flash

«SMS Flash» xizmati bilan saqlanmaydigan SMSlarni to‘g‘ri suhbatdoshing ekraniga yuborishing mumkin!
SMS narxi tarif rejaga binoan

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🕰 SMS Jadval')
async def bot_help(message: types.Message):
    await message.answer(text="""🕰 SMS Jadval

«SMS-jadval» xizmati sen uchun muhim bo‘lgan xabarlarni esdan chiqarmasliginga yordam beradi va avvaldan yetkazish vaqtini belgilaydi!
Vaqtni belgila, matnni yoz, va xabar manzilga kerakli vaqtda yetib boradi!

👉 @aloqa_operatorlar_bot""")