from aiogram import types
from keyboards.default.uzmobile_tariflar import *
from keyboards.default.asosiy_menu import *
from loader import dp


@dp.message_handler(text='📚 Tariflar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_tarif)
@dp.message_handler(text='🔵 Uzmobile')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_asosiy)
@dp.message_handler(text='📓 Street')
async def bot_start(message: types.Message):
    await message.answer(text="""📓 Street

💰 Abonent to‘lovi oyiga 39.900 so‘m

📋 Belgilangan limitlar:
6500 Mb 🌐
750 SMS ✉️
750 Daqiqa O‘zb. bo‘yicha ☎️
1500 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 160 so‘m 
Daqiqa 126 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*1*11*1#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📔 Flash')
async def bot_start(message: types.Message):
    await message.answer(text="""📔 Flash

💰 Abonent to‘lovi oyiga 69.900 so‘m

📋 Belgilangan limitlar:
16 000 Mb 🌐
1500 SMS ✉️
1500 Daqiqa O‘zb. bo‘yicha ☎️
2000 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 160 so‘m 
Daqiqa 84 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi:  *111*1*11*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📒 Royal')
async def bot_start(message: types.Message):
    await message.answer(text="""📒 Royal

💰 Abonent to‘lovi oyiga 149.900 so‘m

📋 Belgilangan limitlar:
Cheksiz Mb 🌐
5000 SMS ✉️
Cheksiz Daqiqa O‘zb. bo‘yicha ☎️
Cheksiz Daqiqa Tarmoq 📞

Limitdan tashqari:
Sms 80 so‘m 

Tarifga o‘tish kodi: *111*1*11*3#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📕 Ishbilarmon')
async def bot_start(message: types.Message):
    await message.answer(text="""📕 Ishbilarmon

💰 Abonent to‘lovi oyiga 99.900 so‘m

📋 Belgilangan limitlar:
25 000 Mb 🌐
3000 SMS ✉️
Cheksiz Daqiqa O‘zb. bo‘yicha ☎️
Cheksiz Daqiqa Tarmoq 📞

Limitdan tashqari:
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*1*11*10#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📘 Oddiy 10')
async def bot_start(message: types.Message):
    await message.answer(text="""📘 Oddiy 10

💰 Abonent to‘lovi oyiga 10 000 so‘m

📋 Belgilangan limitlar:
10 Mb 🌐
10 SMS ✉️
10 Daqiqa ☎️


Limitdan tashqari:
Barchasi 10 so‘m

Tarifga o‘tish kodi: *111*1*11*12#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📗 Onlime')
async def bot_start(message: types.Message):
    await message.answer(text="""📗 Onlime

💰 Abonent to‘lovi oyiga 49.900 so‘m

📋 Belgilangan limitlar:
10 000 Mb 🌐
1000 SMS ✉️
1000 Daqiqa O‘zb. bo‘yicha ☎️
2000 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 280 so‘m 
Daqiqa 84 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*1*11*6#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📙 Yoshlar')
async def bot_start(message: types.Message):
    await message.answer(text="""📙 Yoshlar

💰 Abonent to‘lovi oyiga 5000 so‘m

📋 Belgilangan limitlar:
500 Daqiqa  📞

Limitdan tashqari:
Mb 25 so‘m 
Daqiqa 25 so‘m 
Sms 25 so‘m 

Tarif rejaga faqat jismoniy shaxslar ulanishi mumkin va O‘zbekiston Yoshlar Ittifoqi a’zolari uchun mo‘ljallangan.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="🎓 Ta'lim")
async def bot_start(message: types.Message):
    await message.answer(text="""🎓 Ta'lim

💰 Abonent to‘lovi oyiga 34.900 so‘m

📋 Belgilangan limitlar:
8000 Mb 🌐
500 SMS ✉️
300 Daqiqa O‘zb. bo‘yicha ☎️
1000 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 40 so‘m 
Daqiqa 40 so‘m 
Sms 84 so‘m 

“TA‘LIM” tarif rejasi oliy va o‘rta maxsus o‘quv yurtlari (institutlar, universitetlar, litseylar, kollejlar) talabalari va o‘qituvchilari, shuningdek maktab o‘qituvchilari uchun mo‘ljallangan. Ulanishda talabalar talabalik guvohnomasini va o‘qituvchilar esa guvohnomalarini taqdim etishlari kerak.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📚 Maktab')
async def bot_start(message: types.Message):
    await message.answer(text="""📚 Maktab

💰 Abonent to‘lovi oyiga 29.900 so‘m

📋 Belgilangan limitlar:
5000 Mb 🌐
500 SMS ✉️
200 Daqiqa O‘zb. bo‘yicha ☎️
500 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 40 so‘m 
Daqiqa 40 so‘m 
Sms 84 so‘m 

“MAKTAB” tarif rejasi maktab o‘quvchilari uchun mo‘ljallangan bo‘lib, xizmatni rasmiylashtirish ota-onalardan biriga bolaning tug‘ilganlik haqidagi guvohnomasi taqdim etilganda amalga oshiriladi.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🚀 Street Upgrade')
async def bot_start(message: types.Message):
    await message.answer(text="""📓 Street

💰 Abonent to‘lovi 3 oyga  119.700 so‘m

📋 3 oylik limitlar:
26 000 Mb 🌐
3000 SMS ✉️
3000 Daqiqa O‘zb. bo‘yicha ☎️
6000 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 160 so‘m 
Daqiqa 126 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*1*11*4#
O‘tish narxi 4200 so‘m
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='✈️ Flash Upgrade')
async def bot_start(message: types.Message):
    await message.answer(text="""✈️ Flash Upgrade

💰 Abonent to‘lovi 3 oyga  209.700 so‘m

📋 3 oylik limitlar:
64 000 Mb 🌐
6000 SMS ✉️
6000 Daqiqa O‘zb. bo‘yicha ☎️
8000 Daqiqa Tarmoq 📞

Limitdan tashqari:
Mb 160 so‘m 
Daqiqa 84 so‘m 
Sms 84 so‘m 

Tarifga o‘tish kodi: *111*1*11*5#
O‘tish narxi 4200 so‘m
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👼 Bolajon')
async def bot_start(message: types.Message):
    await message.answer(text="""👼 Bolajon

💰 Abonent to‘lovi oyiga 18.000 so‘m

📋 Belgilangan limitlar:
2000 Mb 🌐
200 SMS ✉️
200 Daqiqa  ☎️

Limitdan tashqari:
Mb 8 so‘m 
Daqiqa 20 so‘m 
Sms 20 so‘m 

Tarif reja faqatgina jismoniy shaxslarga va yangi ulangandagina amal qiladi. Tarif bolalar uchun mo‘ljallangan bo‘lib, ushbu tarifda raqam ota-onalardan birining nomiga rasmiylashtiriladi.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⬅️ Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_asosiy)
@dp.message_handler(text='🛸 Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_internet)
@dp.message_handler(text='🔙 Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_internet)

@dp.message_handler(text='🔰 Oylik internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=oylik_internet_uzmobie)
@dp.message_handler(text='♻️ Internet non-stop')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=non_stop_internet)
@dp.message_handler(text='🗓 TAS-IX uchun Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=tas_ix_internet)
@dp.message_handler(text='🌞 Kunlik Internet')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=kunlik_internet)
@dp.message_handler(text='⬅️ Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_asosiy)
@dp.message_handler(text='♻️ 3 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 3 000 MB non-stop

🌐 3000 MB
💰 To'plam narxi: 24 000 so'm
➡️ Keyingi oylardan: 21 600 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10055*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 5 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 5 000 MB non-stop

🌐 5000 MB
💰 To'plam narxi: 32 000 so'm
➡️ Keyingi oylardan: 28 800 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10056*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)

👉 @Aloqa_operatorlarBot
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 8 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 8 000 MB non-stop

🌐 8000 MB
💰 To'plam narxi: 41 000 so'm
➡️ Keyingi oylardan: 36 900 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10057*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 12 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 12 000 MB non-stop

🌐 12 000 MB
💰 To'plam narxi: 50 000 so'm
➡️ Keyingi oylardan: 45 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10151*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 20 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 20 000 MB non-stop

🌐 20 000 MB
💰 To'plam narxi: 65 000 so'm
➡️ Keyingi oylardan: 58 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10152*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 30 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 30 000 MB non-stop

🌐 30 000 MB
💰 To'plam narxi: 75 000 so'm
➡️ Keyingi oylardan: 67 500 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10153*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ 50 000 MB non-stop')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ 50 000 MB non-stop

🌐 50 000 MB
💰 To'plam narxi: 85 000 so'm
➡️ Keyingi oylardan: 76 500 
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10154*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🗓 TAS-IX 2 048')
async def bot_start(message: types.Message):
    await message.answer(text="""🗓 TAS-IX 2 048

🌐 TAS-IX 2048 MB
💰 To'plam narxi: 15 000 so'm
⏳ Amal qilish muddati: 90 kun
📞 Faollashtirish kodi: *147*10068*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🗓 TAS-IX 10 240')
async def bot_start(message: types.Message):
    await message.answer(text="""🗓 TAS-IX 10 240

🌐 TAS-IX 10 240 MB
💰 To'plam narxi: 40 000 so'm
⏳ Amal qilish muddati: 90 kun
📞 Faollashtirish kodi: *147*10069*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text=' TAS-IX 15 360')
async def bot_start(message: types.Message):
    await message.answer(text="""🗓 TAS-IX 15 360

🌐 TAS-IX 15 360 MB
💰 To'plam narxi: 50 000 so'm
⏳ Amal qilish muddati: 90 kun
📞 Faollashtirish kodi: *147*10070*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌞 100 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🌞 100 MB

🌐 100 MB
💰 To'plam narxi: 3000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *147*10043*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌞 300 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🌞 300 MB

🌐 300 MB
💰 To'plam narxi: 6000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *147*10050*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌞 600 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🌞 600 MB

🌐 600 MB
💰 To'plam narxi: 9000 so'm
⏳ Amal qilish muddati: 1 kun
📞 Faollashtirish kodi: *147*10051*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 1000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 1000 MB

🌐 1000 MB
💰 To'plam narxi: 9000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10072*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 1500 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 1500 MB

🌐 1500 MB
💰 To'plam narxi: 14 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10073*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 3000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 3 000 MB

🌐 3000 MB
💰 To'plam narxi: 18 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10074*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 5000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 5 000 MB

🌐 5000 MB
💰 To'plam narxi: 25 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10075*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 8000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 8 000 MB

🌐 8000 MB
💰 To'plam narxi: 35 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10076*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 12000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 12 000 MB

🌐 12 000 MB
💰 To'plam narxi: 50 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10077*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 12000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 12 000 MB

🌐 12 000 MB
💰 To'plam narxi: 50 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10077*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 20000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 20 000 MB

🌐 20 000 MB
💰 To'plam narxi: 65 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10078*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 30000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 30 000 MB

🌐 30 000 MB
💰 To'plam narxi: 75 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10079*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 50000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 50 000 MB

🌐 50 000 MB
💰 To'plam narxi: 85 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10080*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔰 75000 MB')
async def bot_start(message: types.Message):
    await message.answer(text="""🔰 75 000 MB

🌐 75 000 MB
💰 To'plam narxi: 110 000 so'm
⏳ Amal qilish muddati: 30 kun
📞 Faollashtirish kodi: *147*10150*40149#
(koddan nusxa olish uchun kodning ustiga bosing!)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🛠 Boshqa xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_boshqa_hizmat)
@dp.message_handler(text='✅ Asosiy xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=boshqa_hizmat_asosiy)
@dp.message_handler(text='☑️ Qo‘shimcha xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=boshqa_hizmat_qoshimcha)
@dp.message_handler(text='📩SMS xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=boshqa_hizmat_sms1)
@dp.message_handler(text='🔙  Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=uzmobile_boshqa_hizmat)
@dp.message_handler(text='🗣 Ovozli pochta')
async def bot_start(message: types.Message):
    await message.answer(text="""🗣 Ovozli pochta

Qulay “Ovozli pochta” xizmati endi UZTELECOM mobil abonentlari uchun mavjud. 
Xabar narxi - 240 so'm. Ovozli xabarning maksimal davomiyligi 60 soniya.

Xizmatni faollashtirish kodi: 
*111*1*24*1#

Xizmatni o'chirish kodi:
*111*1*24*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👁 Yashirin qo‘ng‘iroq')
async def bot_start(message: types.Message):
    await message.answer(text="""👁 Yashirin qo‘ng‘iroq

Mazkur xizmat abonentlarga o‘z telefon raqamlarini yashirishga ruhsat beradi.

Xizmat narxi 1 daqiqa uchun 210 so‘m.

Xizmatdan foydalanish uchun terilayotgan raqam oldidan # belgisini tering! 
M: #99899ХХХХХХХ
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='↗️ Qo‘ng‘iroqni boshqa raqamga yo‘naltirish')
async def bot_start(message: types.Message):
    await message.answer(text="""↗️ Qo‘ng‘iroqni boshqa raqamga yo‘naltirish

Xizmatdan foydalanish: **21*telefon raqami#
M: **21*+998991234567# 

Telefon band bo‘lganda **67*telefon raqami#

Javobsiz qo‘ng‘iroqlarda **61* telefon raqami **X# 
Bu yerda X = vaqt, sekundda (5 sekunddan 25 sekundgacha)

Xizmatni o`chirish: ##21#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='❌ Shaxsiy raqam uzatilishini taqiqlash')
async def bot_start(message: types.Message):
    await message.answer(text="""❌ Shaxsiy raqam uzatilishini taqiqlash

Qo‘ng‘iroq qabul qilayotgan abonent telefonida raqam o‘rniga “Raqam yashirilgan”, “Maxfiy raqam” yoki telefon apparati turiga ko‘ra, shunga o‘xshash yozuv chiqadi. 

Xizmat to‘lovi oyiga 8 400 so‘m

Xizmatni yoqish kodi:
*111*2*6#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⏳ Chaqiruvni kutish')
async def bot_start(message: types.Message):
    await message.answer(text="""⏳ Chaqiruvni kutish

«Chaqiruvni kutish» (ikkinchi liniya) xizmati bir qo‘ng‘iroq davomida boshqa qo‘ng‘iroqqa javob berishga imkon beradi.

Xizmatni faollashtirish kodi: 
*43# 📞
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔄 Foydali almashinuv')
async def bot_start(message: types.Message):
    await message.answer(text="""🔄 Foydali almashinuv

Almashuv turi⬇️|      Miqdori   ⬇️ |narxi|   ⬇️kodi|
Daqiqalar MB ga|100 daq => 100 МB|1000|*545*1*1#|
Daqiqalar MB ga|200 daq => 200 МB|2000|*545*1*2#|
Daqiqalar MB ga|500 daq => 500 МB|5000|*545*1*3#|
MB  daqiqalarga|100 МB => 100 daq|1000|*545*2*1#|
MB  daqiqalarga|200 МB => 200 daq|2000|*545*2*2#|
MB  daqiqalarga|500 МB => 500 daq|5000|*545*2*3#|
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔊 «Limitsiz ovoz»')
async def bot_start(message: types.Message):
    await message.answer(text="""🔊 «Limitsiz ovoz»

Xizmat abonentlarga GSM va CDMA tarmoqlari ichida bepul qo‘ng‘iroqlarni amalga oshirish imkonini beradi.

Xizmatni faollashtirish kodi: 
*111*1/2/3*15*1#

Xizmatni o'chirish kodi:
*111*1/2/3*15*2# 
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🤝 Qo‘llab yubor')
async def bot_start(message: types.Message):
    await message.answer(text="""🤝 Qo‘llab yubor

Muvafaqqiyatli pul o‘tkazmasi uchun xizmat narxi 500 so‘m

Xizmatni faollashtirish kodi: 
*122*99XXXXXXX * trafik# 
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌌 Tungi Internet')
async def bot_start(message: types.Message):
    await message.answer(text="""🌌 Tungi Internet

Tun    => narxi 3 999 so‘m   => kodi:  *111*1*18*1#
7 tun  => narxi 19 999 so‘m  => kodi:  *111*1*18*3#
30 tun => narxi 69 999 so‘m  => kodi:  *111*1*18*2#

Kunlik cheklanmagan tezlikdagi  internet trafigi chegarasi 12 000 МB ni tashkil etadi. Limitdan oshsa tezlik 64 Kbit/s
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='💰 EXTRA balans')
async def bot_start(message: types.Message):
    await message.answer(text="""💰 EXTRA balans

Mazkur xizmatdan 150 qisqa raqamiga SMS-so‘rov yuborish yoki *150# qisqa raqamida mavjud USSD-menyu yordamida foydalanish mumkin.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='☎️ Tungi qo’ng’iroqlar')
async def bot_start(message: types.Message):
    await message.answer(text="""☎️ Tungi qo’ng’iroqlar

Qulay “Ovozli pochta” xizmati endi UZTELECOM mobil abonentlari uchun mavjud. 
Xabar narxi - 240 so'm. Ovozli xabarning maksimal davomiyligi 60 soniya.

Xizmatni faollashtirish kodi: 
*111*1/2/3*16*1# 

Xizmatni o'chirish kodi:
*111*1/2/3*16*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♻️ Restart')
async def bot_start(message: types.Message):
    await message.answer(text="""♻️ Restart

Xizmat Street, Flash, Royal, OnLime, Street Ugrade, Flash Upgrade, Ta'lim, MAKTAB, UNITS tarif rejalari uchun amal qiladi.

Xizmatni faollashtirish kodi: 
*555# 
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📚 «ZiyoNET»')
async def bot_start(message: types.Message):
    await message.answer(text="""📚 «ZiyoNET»

«ZiyoNET» xizmatining maqsadi - yoshlarga va o'sib kelayotgan avlodga ta'limga oid manbaalardan foydalanishni tashkillashtirish.

Xizmatni faollashtirish narxi 420 so‘m

Xizmat abonent to‘lovi, kuniga 210 so‘m

Xizmatni faollashtirish kodi: 
*111*2*12*1#

Xizmatni o'chirish kodi:
*111*2*12*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👨‍👩‍👧 «Oila uchun»')
async def bot_start(message: types.Message):
    await message.answer(text="""👨‍👩‍👧 «Oila uchun»

Guruh ichida barcha chiquvchi qo‘ng‘iroqlar – 0 so‘m

«Oila uchun» xizmati guruhi ichida cheklanmagan ovozli trafik 2 100 so‘m

Xizmatni faollashtirish narxi 420 so‘m

Xizmatni faollashtirish kodi: 
*111*1/2/3*17*1*1# 

Xizmatni o'chirish kodi:
*111*1/2/3*17*1*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🧾 YHQ jarimalari haqida xabar')
async def bot_start(message: types.Message):
    await message.answer(text="""🧾 YHQ jarimalari haqida xabar

GSM jismoniy va yuridik shaxslar abonentlar uchun ulanish xizmati.

YHQ buzilishi haqidagi 1 SMS narxi: 210,52 so'm

YHQ buzilishi mavjud emasligi haqidagi 1 SMS narxi: 84,21 so‘m

O‘z YHQ buzilishlari haqida xabar olish uchun: 8860 raqamiga «avtomobilning davlat raqami oraliq bo‘sh joy qoldirish tex. pasport seriyasi va raqami» (Masalan: 01R999XY AAC5447770).
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔁 Tezkor o‘tkazmalar')
async def bot_start(message: types.Message):
    await message.answer(text="""🔁 Tezkor o‘tkazmalar

“Tezkor o‘tkazmalar” xizmati UZTELECOM abonentlari o‘rtasida pul o‘tkazmalarini amalga oshirishga yordam beradi

Muvafaqqiyatli pul o‘tkazmasi uchun xizmat narxi 160 so‘m

USSD orqali pul o‘tkazmalarini amalga oshirish:
*124*3*99XXXABCD# (3=3000 so‘m)

Xizmatni o'chirish kodi:
*111*1/2/3*16*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='♥️ Sevimli raqamlar')
async def bot_start(message: types.Message):
    await message.answer(text="""♥️ Sevimli raqamlar

Yaqin va azizlaringiz bilan doimo aloqada bo‘ling. “Sevimli raqamlar” xizmatini o‘rnating va yaqinlaringiz bilan cheklovsiz muloqotda bo‘ling!

«Sevimli raqamlar» o‘rnatish (har bir o‘rnatilgan raqam uchun) 420 so'm

Abonent to‘lovi, kuniga (har bir o‘rnatilgan raqam uchun) 210 so'm

Xizmatni faollashtirish: 
999131 raqamiga “Sevimli raqam” telefon raqamini xalqaro formatda SMS tarzda yuboring M: 998XXXXXXXXX

Xizmatni o'chirish:
999130 raqamiga “Sevimli raqam” telefon raqamini xalqaro formatda SMS tarzda yuboring m: 998XXXXXXXXX
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⚠️ «Qabul qilinmagan qo‘ng‘iroq» va «Tarmoqda»')
async def bot_start(message: types.Message):
    await message.answer(text="""⚠️ «Qabul qilinmagan qo‘ng‘iroq» va «Tarmoqda»

Endi UZTELECOM GSM abonentlari “Qabul qilinmagan qo‘ng‘iroq” xizmati orqali telefoni o‘chiq bo‘lganda yoki tarmoqdan tashqari bo‘lgan hollarda qabul qilinmagan qo‘ng‘iroqlar haqida ma’lumotga ega bo‘lishlari mumkin.

Xizmat abonent to‘lovi, kuniga 40 so‘m

Xizmatni faollashtirish kodi: 
*111*1*4*1#

Xizmatni o'chirish kodi:
*111*1*4*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 Oylik SMS-paketlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=oylik_sms_paketlar)
@dp.message_handler(text='✉️ Har kunlik SMS')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=kunlik_sms)
@dp.message_handler(text='📨 Xalqaro SMS-paketlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=xalqaro_sms)
@dp.message_handler(text='📩 MS 10 SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 MS 10 SMS

💰 Narxi: 420 so‘m
📨 SMS soni: 10 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*1*1#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 MS 50 SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 MS 50 SMS

💰 Narxi: 1680 so‘m
📨 SMS soni: 50 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*1*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 MS 200 SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 MS 200 SMS

💰 Narxi: 5200 so‘m
📨 SMS soni: 200 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*1*3#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 MS 500 SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 MS 500 SMS

💰 Narxi: 9500 so‘m
📨 SMS soni: 500 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*1*4#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='◀️ Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=boshqa_hizmat_sms1)
@dp.message_handler(text='✉️ 50 SMS Daily')
async def bot_start(message: types.Message):
    await message.answer(text="""✉️ 50 SMS Daily

💰 Narxi: 420 so‘m
📨 SMS soni: 50 
📲 Faollashtirish kodi: *111*1*19*1*1#
❌ O‘chirish kodi: *111*1*19*1*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='✉️ 100 SMS Daily')
async def bot_start(message: types.Message):
    await message.answer(text="""✉️ 100 SMS Daily

💰 Narxi: 840  so‘m
📨 SMS soni: 100 
📲 Faollashtirish kodi: *111*1*19*2*1#
❌ O‘chirish kodi: *111*1*19*1*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 MS 10 MN SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📨 MS 10 MN SMS

💰 Narxi: 9900 so‘m
📨 SMS soni: 10 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*2*1#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 MS 20 MN SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📨 MS 20 MN SMS

💰 Narxi: 18 000 so‘m
📨 SMS soni: 20 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*2*2#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 MS 30 MN SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📨 MS 30 MN SMS

💰 Narxi: 24 800 so‘m
📨 SMS soni: 30 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*2*3#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 MS 40 MN SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📨 MS 40 MN SMS

💰 Narxi: 29 700 so‘m
📨 SMS soni: 40 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*2*4#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📨 MS 50 MN SMS')
async def bot_start(message: types.Message):
    await message.answer(text="""📨 MS 50 MN SMS

💰 Narxi: 33 000 so‘m
📨 SMS soni: 50 
⏳ Muddati: 30 kun
📲 Faollashtirish kodi: *111*1*2*5#
👉 @aloqa_operatorlar_bot""")


