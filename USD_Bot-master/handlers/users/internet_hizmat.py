from aiogram import types
from keyboards.default.qoshimcha_hizmat import *
from keyboards.default.usel_tariflar import *
from loader import dp


@dp.message_handler(text='🌐 Internet hizmatlar')
async def bot_help(message: types.Message):
    await message.answer(text='🌐 Internet hizmatlar',reply_markup=internet_hizmat_button)
@dp.message_handler(text='🌐 Internet')
async def bot_help(message: types.Message):
    await message.answer(text='🌐 Internet',reply_markup=internet_hizmat)

@dp.message_handler(text='🌐 Do it!')
async def bot_help(message: types.Message):
    await message.answer(text="""🌐 Do It!
Chinakam cheksiz tungi Internet!

Kunlik foydalanish uchun to‘lov 5 000 so'm/kun
Ulanish uchun hisobdagi minimal mablag‘ miqdori
5 250 so'm

Ulanish kodi: *100500#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⚔️ Muloqot ulashing')
async def bot_help(message: types.Message):
    await message.answer(text="""↗️Muloqot ulashing!

Tarmoq ichidagi qo‘ng‘iroqlar uchun daqiqalar yuborish kodi:
*203*99890(91)XXX-XX-XX*1# (30 daq.) 
*203*99890(91)XXX-XX-XX*2# (100 daq.)

O‘zbekisto bo‘ylab qo‘ng‘iroqlar uchun daqiqalar yuborish kodi:
*204*99890(91)XXX-XX-XX*1# (30 daq.) 
*204*99890(91)XXX-XX-XX*2# (100 daq.)

Barcha yo‘nalishga MB yuborish kodi:
*205*99890(91)XXX-XX-XX*1# (100 MB) 
*205*99890(91)XXX-XX-XX*2# (200 MB)

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔁 Daqiqalar va megabaytlarni almashtirish')
async def bot_help(message: types.Message):
    await message.answer(text="""🔁 Daqiqalar va megabaytlarni almashtirish

Daqiqalarni megabaytlarga almashtirish:
*200*1# - 100 MB
*200*2# - 400 MB

Megabaytlarni daqiqalarga almashtirish:
*201*1# - O‘zbekiston bo'ylab 100 daqiqa
*201*2# - O‘zbekiston bo'ylab 200 daqiqa

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🚓 «Extra 200»')
async def bot_help(message: types.Message):
    await message.answer(text="""🚓 «Extra 200»
Daqiqa va MB lar bitta paketda!

To‘plam narxi - 10 000 so'm/30 kunga
Internet - 200 MB/30 kunga
Muloqot uchun - 200 daq/30 kunga

Ulanish kodi: *110*500# 

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📹 «IMO 20»')
async def bot_help(message: types.Message):
    await message.answer(text="""📹 «IMO 20»
Yanada manfaatli qo'ng'iroqlar!

20 soatli suhbat 30 kun ichida
Ulanish narxi 5 000 so'm/30 kunga
Ulanish uchun hisobdagi minimal mablag’ miqdori 5 250 so'm

Ulanish kodi: *110*45#


👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🚓 «Extra 400»')
async def bot_help(message: types.Message):
    await message.answer(text="""🚓 «Extra 400»
Daqiqa va MB lar bitta paketda!

To‘plam narxi - 18 000 so'm/30 kunga
Internet - 400 MB/30 kunga
Muloqot uchun - 400 daq/30 kunga

Ulanish kodi: *110*501#

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🚓 «Extra 600»')
async def bot_help(message: types.Message):
    await message.answer(text="""🚓 «Extra 600»
Daqiqa va MB lar bitta paketda!

To‘plam narxi - 25 000 so'm/30 kunga
Internet - 600 MB/30 kunga
Muloqot uchun - 600 daq/30 kunga

Ulanish kodi: *110*502#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🟢 Hamma tarmoqda')
async def bot_help(message: types.Message):
    await message.answer(text="""🟢 Hamma tarmoqda
Ijtimoiy tarmoqlarning mobil versiyalarida do’stlaring bilan kun bo’yi bepul muloqot qil!

Narxi 1 900 so'm/kun

Ulanish kodi: *110*79#

👉 @aloqa_operatorlar_bot""")