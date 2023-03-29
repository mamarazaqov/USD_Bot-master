from aiogram import types
from keyboards.default.mobiuz import *
from keyboards.default.asosiy_menu import *
from loader import dp


@dp.message_handler(text='🔻 MobiUz')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_asosiy)
@dp.message_handler(text='📕 Tariflar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_taroflar)
@dp.message_handler(text='🔻 Mobi 20')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 20

💰 Abonent to‘lovi oyiga/kunlik 20 000/1000 so‘m

📋 Belgilangan limitlar:
2000/67 Mb 🌐
500/17 SMS ✉️
500/17 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 126 so‘m 
Daqiqa / Sms 42 so‘m 

Tarifga o‘tish kodi: *111*120#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 30')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 30

💰 Abonent to‘lovi oyiga 30 000 so‘m

📋 Belgilangan limitlar:
5000 Mb 🌐
1000 SMS ✉️
1000 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa / SMS 84 so‘m 

Tarifga o‘tish kodi: *111*128#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 40')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 40

💰 Abonent to‘lovi oyiga/kunlik 40 000/2000 so‘m

📋 Belgilangan limitlar:
8000/267 Mb 🌐
1200/40 SMS ✉️
1200/40 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 126 so‘m 
Daqiqa / SMS 42 so‘m 

Tarifga o‘tish kodi: *111*122#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 50')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 50

💰 Abonent to‘lovi oyiga 50 000 so‘m

📋 Belgilangan limitlar:
10 000 Mb 🌐
1500 SMS ✉️
1500 Daqiqa O‘zb. bo‘yicha ☎️
Cheksiz daqiqalar tarmoq ichida 📞

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa / SMS 84 so‘m 

Tarifga o‘tish kodi: *111*129#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 70')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 70

💰 Abonent to‘lovi oyiga 70 000 so‘m

📋 Belgilangan limitlar:
20 000 Mb 🌐
2500 SMS ✉️
2500 Daqiqa O‘zb. bo‘yicha ☎️
Cheksiz daqiqalar tarmoq ichida 📞

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa / SMS 84 so‘m 

Tarifga o‘tish kodi: *111*131#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 90')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 90

💰 Abonent to‘lovi oyiga 90 000 so‘m

📋 Belgilangan limitlar:
65 000 Mb 🌐
3500 SMS ✉️
3500 Daqiqa O‘zb. bo‘yicha ☎️
Cheksiz daqiqa tarmoq ichida 📞

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa / SMS 84 so‘m 

Tarifga o‘tish kodi: *111*132#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 110')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 110

💰 Abonent to‘lovi oyiga 110 000 so‘m

📋 Belgilangan limitlar:
80 000 Mb 🌐
5000 SMS ✉️
Cheksiz Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 421 so‘m 
SMS 84 so‘m 

Tarifga o‘tish kodi: *111*133#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔻 Mobi 150')
async def bot_start(message: types.Message):
    await message.answer(text="""🔻 Mobi 150

💰 Abonent to‘lovi oyiga 150 000 so‘m

📋 Belgilangan limitlar:
100 000 Mb 🌐
10 000 SMS ✉️
Cheksiz Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 421 so‘m / SMS 84 so‘m 

Tarifga o‘tish kodi: *111*134#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='✅ Yengil')
async def bot_start(message: types.Message):
    await message.answer(text="""✅ Yengil

💰 Abonent to‘lovi oyiga/kunlik 8000/400 so‘m

📋 Belgilangan limitlar:
80/3 Mb 🌐
80/3 SMS ✉️
80/3 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
1 Mb / 1 Daqiqa / 1 SMS - 8 so‘m 

Tarif rejasiga 2021-yilning 31-mart sanasigacha (shu jumladan) ulanish mumkin
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👌 GAP yo‘q')
async def bot_start(message: types.Message):
    await message.answer(text="""👌 GAP yo‘q

💰 Abonent to‘lovi oyiga/kunlik 35 000/1750 so‘m

📋 Belgilangan limitlar:
10 000/334 Mb 🌐
1 Daqiqa / 1 SMS - 12 so‘m

Limitdan tashqari:
1 Mb 12 so‘m

Tarifga o‘tish kodi: *111*100#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👌 GAP yo‘q Pro')
async def bot_start(message: types.Message):
    await message.answer(text="""👍 GAP yo‘q Pro

💰 Abonent to‘lovi oyiga/kunlik 75 000/3750 so‘m

📋 Belgilangan limitlar:
35 000/1167 Mb 🌐
25 000/834 Mb tungi 🌐
(00.00 dan 08.00 gacha)
1000/34 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Daqia/SMS/MB - 12 so‘m

Tarifga o‘tish kodi: *111*101#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🖨 Terminal')
async def bot_start(message: types.Message):
    await message.answer(text="""🖨 Terminal

💰 Abonent to‘lovi oyiga  12 000 so‘m

📋 Oylik limit:
300 Mb 🌐

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa 126 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi:  *111*112#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌞 Chilla Lite')
async def bot_start(message: types.Message):
    await message.answer(text="""🌞 Chilla Lite

💰 Abonent to‘lovi oyiga  20 000 so‘m

📋 3 oylik limitlar:
200 Mb 🌐
100 SMS ✉️
3000 Daqiqa O‘zb. bo‘yicha ☎️

Limitdan tashqari:
Mb 421 so‘m 
Daqiqa 84 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*042#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⏪ Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_asosiy)
@dp.message_handler(text='📶 Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_internet)
@dp.message_handler(text='📡 Oylik Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_oylik_internet)
@dp.message_handler(text='🏎 «Tungi DRIVE»')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_tungi_drive)
@dp.message_handler(text='🌌 Tungi internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_tungi_internet)
@dp.message_handler(text='🌅 Kunlik Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_kunlik_internet)
@dp.message_handler(text='🟢 «OnNet»')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_onnet)
@dp.message_handler(text='↩️ Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_internet)
@dp.message_handler(text='📡 300 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 300 MB

🌐 3000 MB
💰 To'plam narxi: 8000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*1*010300272*1#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 500 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 500 MB

🌐 500 MB
💰 To'plam narxi: 9000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*7*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 1000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 1000 MB

🌐 1000 MB
💰 To'plam narxi: 11 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*1*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 2000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 2000 MB

🌐 2000 MB
💰 To'plam narxi: 17 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*1*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 3000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 3000 MB

🌐 3000 MB
💰 To'plam narxi: 25 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*3*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 5000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 5000 MB

🌐 5 000 MB
💰 To'plam narxi: 33 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*4*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📡 10000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 10000 MB

🌐 10 000 MB
💰 To'plam narxi: 50 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*6*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📡 20000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 20000 MB

🌐 20 000 MB
💰 To'plam narxi: 55 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*8*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📡 30000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 30000 MB

🌐 30 000 MB
💰 To'plam narxi: 65 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*9*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📡 50000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""📡 50000 MB

🌐 50 000 MB
💰 To'plam narxi: 75 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*019*10*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🏎 Tungi DRIVE 1')
async def bot_start(message: types.Message):
    await message.answer(text="""🏎 Tungi DRIVE 1

«Tungi DRIVE» xizmati abonentlarga har tun soat 00:00dan 08:00gacha internetdan cheksiz foydalanish imkonini beradi

💰 Xizmat narxi: 5000 so'm
🌐 chekiz internet
⏳ Amal qilish muddati: 1 tun
📞 Faollashtirish kodi: *171*200*1*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🏎 Tungi DRIVE 7')
async def bot_start(message: types.Message):
    await message.answer(text="""🏎 Tungi DRIVE 7

«Tungi DRIVE» xizmati abonentlarga har tun soat 00:00dan 08:00gacha internetdan cheksiz foydalanish imkonini beradi

💰 Xizmat narxi: 20 000 so'm
🌐 chekiz internet
⏳ Amal qilish muddati: 7 tun
📞 Faollashtirish kodi: *171*200*7*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🏎 Tungi DRIVE 30')
async def bot_start(message: types.Message):
    await message.answer(text="""🏎 Tungi DRIVE 30

«Tungi DRIVE» xizmati abonentlarga har tun soat 00:00dan 08:00gacha internetdan cheksiz foydalanish imkonini beradi

💰 Xizmat narxi: 60 000 so'm
🌐 chekiz internet
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*200*30*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 1 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 1 000

🌐 1000 MB
💰 To'plam narxi: 5 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*1000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 2 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 2 000

🌐 2000 MB
💰 To'plam narxi: 9 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*2000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 3 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 3 000

🌐 3000 MB
💰 To'plam narxi: 12 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*3000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 5 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 5 000

🌐 5000 MB
💰 To'plam narxi: 17 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*5000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 10 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 10 000

🌐 10 000 MB
💰 To'plam narxi: 22 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*10000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 20 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 20 000

🌐 20 000 MB
💰 To'plam narxi: 33 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*20000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌌 Tungi 50 000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi 50 000

🌐 50 000 MB
💰 To'plam narxi: 44 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *171*203*50000*010300272*1#
(kodni ustiga bosib, kopiya qilib olish mumkin.)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 200')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 200

🌐 200 MB
💰 To'plam narxi: 2000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*200*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)

👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 300')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 300

🌐 300 MB
💰 To'plam narxi: 3000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*300*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 500')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 500

🌐 500 MB
💰 To'plam narxi: 4000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*500*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 1000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 1000

🌐 1000 MB
💰 To'plam narxi: 5000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*500*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 2000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 2000

🌐 2000 MB
💰 To'plam narxi: 9000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*2000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 3000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 3000

🌐 3000 MB
💰 To'plam narxi: 12000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*3000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 5000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 5000

🌐 5000 MB
💰 To'plam narxi: 16 500 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*5000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🌅 Kunlik 10000')
async def bot_start(message: types.Message):
    await message.answer(text="""🌅 Kunlik 10 000

🌐 10000 MB
💰 To'plam narxi: 25000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *171*204*10000*010300272*1#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 300 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 300 MB

🌐 300 MB
💰 To'plam narxi: 8000 so'm
➡️ Keyingi oydan narxi: 7200 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*300#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 500 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 500 MB

🌐 500 MB
💰 To'plam narxi: 9000 so'm
➡️ Keyingi oydan narxi: 8100 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*500#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 1000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 1000 MB

🌐 1000 MB
💰 To'plam narxi: 11 000 so'm
➡️ Keyingi oydan narxi: 9 900 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*1000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 2000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 2000 MB

🌐 2000 MB
💰 To'plam narxi: 17000 so'm
➡️ Keyingi oydan narxi: 15 300 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*2000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 3000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 3000 MB

🌐 3000 MB
💰 To'plam narxi: 25000 so'm
➡️ Keyingi oydan narxi: 22 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*3000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 5000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 5000 MB

🌐 5000 MB
💰 To'plam narxi: 33000 so'm
➡️ Keyingi oydan narxi: 29 700 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*5000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 10000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 10000 MB

🌐 10 000 MB
💰 To'plam narxi: 50 000 so'm
➡️ Keyingi oydan narxi: 45 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*10000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 20000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 20000 MB

🌐 20 000 MB
💰 To'plam narxi: 55 000 so'm
➡️ Keyingi oydan narxi: 49 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*20000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 30000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 30000 MB

🌐 30 000 MB
💰 To'plam narxi: 65 0000 so'm
➡️ Keyingi oydan narxi: 58 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*30000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🟢 OnNet 50000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🟢 OnNet 50000 MB

🌐 50 000 MB
💰 To'plam narxi: 75 000 so'm
➡️ Keyingi oydan narxi: 67 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *202*50000#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📚 Boshqa xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_boshqa_xizmatlar)
@dp.message_handler(text="📞 Daqiqalar to'plami")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_daqiqalar)
@dp.message_handler(text="📩 SMS-to'plamlar")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=smslar_toplami_mobiuz)
@dp.message_handler(text="💰 Pul o‘tkazish")
async def bot_start(message: types.Message):
    await message.answer(text="""💰 Pul o‘tkazish

Pul jo‘natish uchun:
*112*xalqaro formatdagi abonent raqami*jo‘natma summasi(so‘mda)# qo‘ng‘iroq
Masalan, Toshkent shahridagi 1300909 raqamli abonentga 2500 so‘m  jo‘natmoqchisiz:
*112*998971300909*2500# 📞

Hisobni to‘ldirishga so‘rov yuborish uchun:
*116*xalqaro formatdagi abonent raqami*jo‘natma summasi (so‘mda)# qo‘ng‘iroq
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📲 IMEI-kodni ro‘yxatdan o‘tkazish")
async def bot_start(message: types.Message):
    await message.answer(text="""📲 IMEI-kodni ro‘yxatdan o‘tkazish

Mobil qurilmaning IMEI-kodini bilib olish - *#06#

Mobil qurilmaning IMEI-kodi holatini tekshirish

1. *1170# USSD-so‘rov orqali.

2. 1170 raqamiga IMEI-kod yozilgan SMS xabar yuborish yordamida.

3. UZIMEI yagona ma’lumotlar bazasining rasmiy veb-saytida— www.uzimei.uz;
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 60 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 60 daqiqalik to‘plam

💰 To‘plam narxi - 4000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*60#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 120 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 120 daqiqalik to‘plam

💰 To‘plam narxi - 7000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*120#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 180 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 180 daqiqalik to‘plam

💰 To‘plam narxi - 10 000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*180#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 300 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 300 daqiqalik to‘plam

💰 To‘plam narxi - 16 000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*300#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 900 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 900 daqiqalik to‘plam

💰 To‘plam narxi - 37 000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*900#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 1200 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 1200 daqiqalik to‘plam

💰 To‘plam narxi - 45 000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*1200#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📞 1800 daqiqalik to‘plam")
async def bot_start(message: types.Message):
    await message.answer(text="""📞 1800 daqiqalik to‘plam

💰 To‘plam narxi - 62 000 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *103*1800#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="'📩 «SMS 100»")
async def bot_start(message: types.Message):
    await message.answer(text="""📩 «SMS 100»

💰 To‘plam narxi - 4500 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *104*100#
📩 SMSlar soni - 100 ta.
📱 Qoldiqni tekshirish - *104#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📩 «SMS 300»")
async def bot_start(message: types.Message):
    await message.answer(text="""✉️ «SMS 300»

💰 To‘plam narxi - 10 500 so‘m 
🗓 Muddati - 30 kun
To‘plamni yoqish kodi: *104*300#
📩 SMSlar soni - 300 ta.
📱 Qoldiqni tekshirish - *104#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="↪️ Orqaga")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=mobiuz_asosiy)