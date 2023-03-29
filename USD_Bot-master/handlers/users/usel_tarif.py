from aiogram import types
from keyboards.default.tariflar import *
from keyboards.default.usel_tariflar import *
from keyboards.default.asosiy_menu import *
from loader import dp


@dp.message_handler(text='🗒 Tariflar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_tarif)
@dp.message_handler(text='🚀 Cosmo tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=cosmo_tarif)
@dp.message_handler(text='📲 Special tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=special_tarif)
@dp.message_handler(text='➕ Special+ tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=special_plus_tariflar)
@dp.message_handler(text='🎭 Kayfiyat tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=kayfiyat_tariflar)
@dp.message_handler(text='🎉 Tantana tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=tantana_tarif)
@dp.message_handler(text='🏨 Marhamat tarifi')
async def bot_start(message: types.Message):
    await message.answer(text="""🏨 Marhamat tarifi:

Qo‘ng‘iroqlar - 30 daqiqa 📞
Internet - 30 MB 🌐

Limitdan tashqari:
Qo‘ng‘iroqlar 1 daqiqasi  - 10 so‘m
Internet 1 mb - 10 so‘m
SMS  - 10 so‘m
   
Abonent to`lovi oyiga 10 000 so`m 💰 
Tarif faqat yangi ulanuvchilar uchun amal qiladi
👉 @aloqa_operatorlar_bot    
""")


@dp.message_handler(text='📆 Yengil hafta')
async def bot_start(message: types.Message):
    await message.answer(text="""📆 Yengil hafta tarifi:

Qo‘ng‘iroqlar - 200 daqiqa 📞
Internet -  200 MB 🌐
SMS - 200 ta ✉️
Abonent to`lovi haftasiga 5000 so`m 💰
     
Qoldiqlarni tekshirish: *103#     
Tarifga o`tish  *120#
👉 @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='💼️ Oddiy')
async def bot_start(message: types.Message):
    await message.answer(text="""💼️ Oddiy:

Qo‘ng‘iroqlar 📞 : 
    Tarmoq ichida 1 daqiqasi - 95 so‘m
    O‘zbekiston bo‘yicha 1 daqiqasi- 120 so‘m
SMS ✉️: 
    O‘zbekiston bo‘yicha - 80 so‘m
    Xalqaro chiqvchi sms - 1000 so‘m
Internet 🌐 :
 1 mb  - 450 so‘m 

Abonent to`lovi kuniga - 380 so`m 💰    
Tarifga o`tish: *120#
👉 @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='🎓 Student')
async def bot_start(message: types.Message):
    await message.answer(text="""🎓 Student tarifi:

Qo‘ng‘iroqlar - 700 daqiqa 📞
Internet -  3500 MB 🌐
SMS - 200 ta ✉️
Abonent to`lovi oyiga 10 000 so`m 💰

Qoldiqlarni tekshirish: 
    *103# - internet
    *102# - daqiqa va sms

Tarif faqat yangi ulanuvchilar uchun amal qiladi.
👉 @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='✈️ Uchar internet')
async def bot_start(message: types.Message):
    await message.answer(text="""✈️ Uchar internet tarifi:

Internet trafigi cheksiz 🌐 :
3000 mb tugagach keyingi abonent to‘lovi yechilgunga qadar tezlik 64 kbit/s gacha qilib belgilanadi.  
 
Abonent to`lovi oyiga - 22 000 so`m 💰 
Tarifga o`tish: *120#
👉 @aloqa_operatorlar_bot    
""")


@dp.message_handler(text='<<Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_asosiy)
@dp.message_handler(text='<<<Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_tarif)
@dp.message_handler(text='🛰 Cosmo 16')
async def bot_start(message: types.Message):
    await message.answer(text="""🚀 COSMO 16 tarifi:

Qo‘ng‘iroqlar - 1000 daqiqa 📞
Internet - 2000 MB 🌐
SMS - 200 ta ✉️
Abonent to`lovi oyiga - 16 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='🛰 Cosmo 23')
async def bot_start(message: types.Message):
    await message.answer(text="""🚀 COSMO 23 tarifi:

Qo‘ng‘iroqlar - 1500 daqiqa 📞
Internet - 3000 MB 🌐
SMS - 300 ta ✉️ 
Abonent to`lovi oyiga - 23 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='🛰 Cosmo 28')
async def bot_start(message: types.Message):
    await message.answer(text="""🚀 COSMO 28 tarifi:

Qo‘ng‘iroqlar - 2000 daqiqa 📞
Internet - 5000 MB 🌐
SMS - 500 ta ✉️
Abonent to`lovi oyiga 28 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 35')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 35 tarifi:

Qo‘ng‘iroqlar - 2500 daqiqa 📞
Internet - 7000 MB 🌐
SMS - 1000 ta ✉️
Abonent to`lovi oyiga - 35 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 45')
async def bot_start(message: types.Message):
    await message.answer(text="""📗  SPECIAL 45:

Qo‘ng‘iroqlar - 3000 daqiqa 📞
Internet - 9000 MB 🌐
SMS - 2000 ta ✉️
Abonent to`lovi oyiga - 45 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#

👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 45')
async def bot_start(message: types.Message):
    await message.answer(text="""📗  SPECIAL 45:

Qo‘ng‘iroqlar - 3000 daqiqa 📞
Internet - 9000 MB 🌐
SMS - 2000 ta ✉️
Abonent to`lovi oyiga - 45 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special 55')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 55 tarifi:

Qo‘ng‘iroqlar - 4000 daqiqa 📞
Internet - 12 000 MB 🌐
SMS - 3000 ta ✉️  
Abonent to`lovi oyiga 55 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 70')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 70 tarifi:

Qo‘ng‘iroqlar -  Cheksiz 📞
Internet - 16 000 MB 🌐
SMS - 4 000 ta ✉️
Abonent to`lovi oyiga - 70 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 70')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 70 tarifi:

Qo‘ng‘iroqlar -  Cheksiz 📞
Internet - 16 000 MB 🌐
SMS - 4 000 ta ✉️
Abonent to`lovi oyiga - 70 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special 80')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 80 tarifi:

Qo‘ng‘iroqlar -  Cheksiz daqiqa 📞
Internet - 18000 MB 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga - 80 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#

👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 100')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 100 :

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - 25 000 MB 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga 100 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120# :

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - 25 000 MB 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga 100 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special Unlim')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special Unlim :

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - Cheksiz 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga 139 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special Unlim')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special Unlim :

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - Cheksiz 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga 139 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special Unlim TURBO')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special Unlim TURBO :

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - 📗 Special unlim turbo
SMS - 5000 ta ✉️
Abonent to`lovi oyiga 150 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special 35➕')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 35➕ tarifi:

Qo‘ng‘iroqlar - 2500 daqiqa 📞
Internet - 7000 MB 🌐
SMS - 1000 ta ✉️
Abonent to`lovi oyiga - 37 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 55➕')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 55➕ tarifi:

Qo‘ng‘iroqlar - 4000 daqiqa 📞
Internet - 12 000 MB 🌐
SMS - 3000 ta ✉️ 
Abonent to`lovi oyiga 57 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='📗 Special 80➕')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 80➕ tarifi:

Qo‘ng‘iroqlar -  Cheksiz 📞
Internet - 18000 MB 🌐
SMS - 5000 ta ✉️
Abonent to`lovi oyiga - 82 000 so`m 💰

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📗 Special 125➕')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Special 125➕ tarifi:

Qo‘ng‘iroqlar - Cheksiz 📞
Internet - 35 000 MB 🌐
SMS - 5000 ta ✉️ 
Abonent to`lovi oyiga 127 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text='🎭 Yaxshi kayfiyat')
async def bot_start(message: types.Message):
    await message.answer(text="""🎭 Yaxshi kayfiyat tarifi:

Qo‘ng‘iroqlar 📞 : 
    750 daqiqa tarmoq ichida 
    75 daqiqa tarmoqdan tashqari

Internet 🌐 :
 300 MB umumiy
 1000 MB messenjerlar uchun   
Abonent to`lovi oyiga - 13 000 so`m 💰
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🎭 Zo'r kayfiyat")
async def bot_start(message: types.Message):
    await message.answer(text="""🎭 Zo‘r kayfiyat:

Qo‘ng‘iroqlar 📞 : 
    1000 daqiqa tarmoq ichida 
    150 daqiqa tarmoqdan tashqari

Internet 🌐 :
 500 MB umumiy
 1500 MB messenjerlar uchun 
Abonent to`lovi oyiga - 20 000 so`m 💰
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🎭 A'lo kayfiyat")
async def bot_start(message: types.Message):
    await message.answer(text="""🎭 A'lo kayfiyat:

Qo‘ng‘iroqlar 📞 : 
    1200 daqiqa tarmoq ichida 
    200 daqiqa tarmoqdan tashqari

Internet 🌐 :
 1200 MB umumiy
 2000 MB messenjerlar uchun  
Abonent to`lovi oyiga - 25 000 so`m 💰
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🎉 Tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""🎉 Tantana:

Qo‘ng‘iroqlar - 1000 daqiqa 📞
SMS - 1000 ta ✉️  
Abonent to`lovi oyiga 15 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms   
Tarifga o`tish: *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🎉 Katta tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""🎉 Katta tantana:

Qo‘ng‘iroqlar - 1500 daqiqa 📞
SMS - 1500 ta ✉️
Abonent to`lovi oyiga 20 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms 
    
Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🎉 Super tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""🎉 Super tantana:

Qo‘ng‘iroqlar - 3000 daqiqa 📞
SMS - 3000 ta ✉️   
Abonent to`lovi oyiga 30 000 so`m 💰
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms 
    
Tarifga o`tish uchun *877#
👉 @aloqa_operatorlar_bot
""")


@dp.message_handler(text="🗓 Oylik Internet to‘plamlari")
async def bot_start(message: types.Message):
    await message.answer(text="""🗓 Oylik Internet to‘plamlari:

To‘plam 1 GB - 8 900 so‘m
kod: *558*555*3*1*21691#

To‘plam 1,5 GB - 13 000 so‘m
kod: *558*555*3*2*21691#

To‘plam 2 GB - 15 000 so‘m
kod: *558*555*3*3*21691#

To‘plam 4 GB - 25 000 so‘m
kod: *558*555*3*4*21691#

To‘plam 7 GB - 35 000 so‘m
kod: *558*555*3*5*21691#

To‘plam 10 GB - 45 000 so‘m
kod: *558*555*3*6*21691#

To‘plam 13 GB - 55 000 so‘m
kod: *558*555*3*7*21691#

To‘plam 20 GB - 65 000 so‘m
kod: *558*555*3*8*21691#

To‘plam 30 - 75 000 so‘m
kod: *558*555*3*9*21691#

To‘plam 50 - 85 000 so‘m
kod: *558*555*3*10*21691#

To‘plam 80 - 115 000 so‘m
kod: *558*555*3*11*21691#

To‘plam 90 - 135 000   so‘m
kod: *558*555*3*12*21691#

To‘plam 135 - 188 000   so‘m
kod: *558*555*3*13*21691#

(koddan nusxa olish uchun ustiga bosing!)

MB amal qilish muddati - 31 kun
Trafik qoldig‘ini tekshirish: *107#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="📆 Haftalik Internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""📆 Haftalik Internet-to‘plamlar:

Tarmoqdagi muloqot kamlik qilyaptimi? Unday bo‘lsa biz Sizga ko‘proq Internet taklif qilamiz!

Haftalik 80 to‘plami - 8 420 so‘m - 80 MB - *555*2*1*1#
Haftalik 160 to‘plami - 12 630 so‘m - 160 MB - *555*2*2*1#
Haftalik 320 to‘plami - 16 840 so‘m - 320 MB - *555*2*3*1#
To‘plamni o‘chirish: *555*2*10*2*1# 

Xizmatni boshqarish: *️⃣5️⃣5️⃣5️⃣*️⃣2️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="☀️ Kunlik Internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""
☀️ Kunlik Internet-to‘plamlar:

To‘plam 5 - 390 so‘m - 5 MB - *555*1*1*1#

To‘plam 10 - 550 so‘m - 10 MB - *555*1*2*1#

To‘plam 20 - 790 so‘m - 20 MB - *555*1*3*1#

To‘plam 35 - 1 190 so‘m - 35 MB - *555*1*4*1#

To‘plam 55 - 1 890 so‘m - 55 MB - *555*1*5*1#

To‘plam 100 - 2 790 so‘m - 100 MB - *555*1*6*1#

To‘plam 130 - 3 790 so‘m - 130 MB - *555*1*7*1#

To‘plam 160 - 4 490 so‘m - 160 MB - *555*1*8*1#

To‘plam 200 - 4 990 so‘m - 200 MB - *555*1*9*1#

(koddan nusxa olish uchun ustiga bosing!)
👉 @aloqa_operatorlar_bot
""")

@dp.message_handler(text="➡️Internet-o‘tkazma")
async def bot_start(message: types.Message):
    await message.answer(text="""➡️Internet-o‘tkazma:

Internet-trafikni do‘stingiz bilan baham ko‘ring!
*525*998YYXXXXXXX*internet trafik hajmi(100-300)#
Bitta muvaffaqiyatli o‘tkazma narxi 500 so‘m
*Mablag‘ Internet-trafik jo‘natuvchi-abonent hisobidan ushlab qolinadi.

Xizmatni boshqarish: *️⃣5️⃣2️⃣5️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="💃 Aksiya: 1gb, 2gb, va 3gb")
async def bot_start(message: types.Message):
    await message.answer(text="""💃 Aksiya: 1gb, 2gb, va 3gb:

Qo‘shimcha hamyonbop internet-to‘plamlar

Tarif rejasi bo‘yicha internet-trafigingiz yetmay qoldimi?

Yangi internet-to‘plamlarni kutib oling:

  300 MB atigi 5 000 so‘mga – «COSMO» tariflar tizimi uchun

  1 GB atigi 8 000 so‘mga – «A’lo kayifyat» tarifi va «COSMO» tariflar tizimi uchun

  1.5 GB atigi 15 000 so‘mga – «COSMO» tariflar tizimi uchun

  2 GB atigi 10 000 so‘mga – «Active» va «Special» tariflar tizimlari uchun

  3 GB atigi 15 000 so‘mga – «Active» va «Special» tariflar tizimlari uchun

  4 GB atigi 27 000 so‘mga – «Active» va «Special» tariflar tizimlari uchun

  5 GB atigi 33 000 so‘mga – «Active» va «Special» tariflar tizimlari uchun

Xizmatni boshqarish: *️⃣2️⃣5️⃣5️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="⏳ Soatbay internet")
async def bot_start(message: types.Message):
    await message.answer(text="""⏳ Soatbay internet:

Yirik fayllarni ko‘chirib olish uchun ko‘p trafik kerakmi?
«Soatbay internet» xizmatidan foydalaning va 1 soatga 5 GB internet oling.
Faollashtirish va boshqarish:*️⃣6️⃣1️⃣6️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🌙 Tungi internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""🌙 Tungi internet-to‘plamlar:

Tungi internet-to‘plamlar – bu tungi vaqtda qulay foydalanish uchun hamyonbop narxda ko‘p internet-trafik.
To‘plam 5 GB – 20 000 so‘m
To‘plam 20 GB – 45 000 so‘m

Xizmatdan foydalanish davri: 01:00-09:00
Xizmatning amal qilish muddati: 30 kun

Faollashtirish va boshqarish:*️⃣6️⃣1️⃣6️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="♾ Cheksiz Internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""♾ Cheksiz Internet-to‘plamlar:

Ucelldan yuqori tezlikdagi 4G bilan yangi imkoniyatlar eshigini oching!
Faolashtirish: *️⃣5️⃣5️⃣5️⃣*️⃣4️⃣#️⃣
Xizmatni bekor qilish: *555*4*10*2#
Berilgan trafik limiti tugagandan so‘ng, Internet tezligi 64 Kb/soniyaga teng bo‘ladi.

Xizmatni boshqarish: 
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="✈️ Oylik 4G Internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""✈️ Oylik 4G Internet-to‘plamlar:

Ucell yangi Oylik Internet to‘plamlarini taqdim qilmoqda. To‘plamlardan biriga bir marta ulaning va har 30 kunda yangi to‘plamga ega bo‘ling. To‘plamlar avtomatik tarzda belgilanadi.
To‘plamlarni faollashtirish/boshqarish: *️⃣5️⃣5️⃣5️⃣*️⃣5️⃣#️⃣
Foydalanilgan trafikni tekshirish: *555*5*10*1#
Xizmatni bekor qilish: *555*5*10*2#
Xizmat bekor qilingan holda sarflanmagan Internet-trafik qoldig'i bekor qilinadi.
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="📡 TAS-IX uchun internet-to‘plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""📡 TAS-IX uchun internet-to‘plamlar:

TAS-IX 8000 8000 10 000 30 kun
TAS-IX 14 000 14 000 15 000 30 kun
TAS-IX 20 000 20 000 20 000 30 kun

Xizmatni boshqarish: *️⃣6️⃣1️⃣6️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🎁 Internet-sovg‘a")
async def bot_start(message: types.Message):
    await message.answer(text="""🎁 Internet-sovg‘a:

Yaqinlaringizga quvonch ulashing
Yangi yil ortda qolgan bo‘lsada, kayfiyat bayramona bo‘lib qolaveradi!
Ucellning yangi “Internet-sovg‘a” xizmati bilan hamyonbop narxda yaqinlaringizga internet-to‘plam sovg‘a qilib, ularni xursand etishda davom eting.

Xizmatni boshqarish: *️⃣9️⃣7️⃣9️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="💥 Mega BOOM")
async def bot_start(message: types.Message):
    await message.answer(text="""💥 Mega BOOM:

Internet foydalanuvchilari uchun ajoyib yangilik!

1 MB atigi 4,21 so‘m.
Xizmatni ulash narxi: 421 so‘m
Abonent to‘lovi: 421 so‘m kuniga
Xizmatni yoqish: *️⃣9️⃣0️⃣9️⃣#️⃣
Xizmatni o‘chirish: *️⃣9️⃣0️⃣9️⃣*️⃣2️⃣#️⃣
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="💵 Internet-avans")
async def bot_start(message: types.Message):
    await message.answer(text="""💵 Internet-avans:

Internet-to‘plam xarid qilish imkoniyati yo‘qmi?
"Internet-avans" xizmatidan foydalaning – 30 kun muddatga 50 MB Internet-trafik oling.
"Internet-avans" xizmatidan foydalanganlik uchun to‘lov  - 1 052,5 so‘m (hisobni birinchi to‘ldirishda 50 MB Internet-trafik qiymati bilan birga yechib olinadi).

Xizmatni boshqarish  *️⃣5️⃣1️⃣5️⃣#️⃣yoki *️⃣9️⃣1️⃣1️⃣#️⃣ USSD-buyrug‘i orqali amalga oshiriladi.
👉 @aloqa_operatorlar_bot
""")