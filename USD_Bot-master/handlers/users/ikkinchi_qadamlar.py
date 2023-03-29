from aiogram import types
from keyboards.default.oylik_paket import *
from keyboards.default.tariflar import *
from loader import dp


@dp.message_handler(text="👍 ZO'R 2")
async def bot_start(message: types.Message):
    await message.answer(text="👍 ZO'R 2 tarifi:\n"

                            "Oylik abonent to‘lovi 20 000 so‘m\n"
                            "Qo‘ng‘iroqlar - 2000 daqiqa 📞\n"
                            "Internet - 2000 MB 🌐\n"
                            "SMS - 2000 ta ✉️\n"

                            "Tarifga ulanish kodi  *️⃣1️⃣1️⃣0️⃣*️⃣3️⃣6️⃣#️⃣\n"
                            "👉 @aloqa_operatorlar_bot")
@dp.message_handler(text="👍 ZO'R 6")
async def bot_start(message: types.Message):
    await message.answer(text="👍 ZO'R 6 tarifi:\n"

                            "Oylik abonent to‘lovi 35 000 so‘m\n"
                            "Qo‘ng‘iroqlar - cheksiz 📞\n"
                            "Internet - 6000 MB 🌐\n"
                            "SMS - 5000 ta ✉️\n"

                            "Tarifga ulanish kodi *110*60#\n"
                              "👉 @aloqa_operatorlar_bot")
@dp.message_handler(text="👍 ZO'R 10")
async def bot_start(message: types.Message):
    await message.answer(text="👍 ZO'R 10 tarifi:\n"

                            "Oylik abonent to‘lovi 50 000 so‘m\n"
                            "Qo‘ng‘iroqlar - cheksiz 📞\n"
                            "Internet - 10 000 MB 🌐\n"
                            "SMS - 5000 ta ✉️\n"
                                
                            "Tarifga ulanish kodi *110*38#\n"
                              "👉 @aloqa_operatorlar_bot")
@dp.message_handler(text="👍 ZO'R 15")
async def bot_start(message: types.Message):
    await message.answer(text="""""👍 ZO'R 15 tarifi:\n

Oylik abonent to‘lovi 70 000 so‘m\n
Qo‘ng‘iroqlar - cheksiz 📞\n
Internet - 15 000 MB 🌐\n
SMS - 5000 ta ✉️\n

Tarifga ulanish kodi *110*39#\n
"👉 @aloqa_operatorlar_bot""""")
@dp.message_handler(text="📞 ALLO")
async def bot_start(message: types.Message):
    await message.answer(text="""""📞 ALLO

Oylik abonent to‘lovi 15 000 so‘m
Qo‘ng‘iroqlar - 600 daqiqa 📞
SMS - 600 ta ✉️

Kunlik abonent to‘lovi 600 so‘m
Qo‘ng‘iroqlar - 20 daqiqa 📞
SMS - 20 ta ✉️

Tarifga ulanish kodi *110*40#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📅 Kunlik")
async def bot_start(message: types.Message):
    await message.answer(text="""""📅 Kunlik

Kunlik abonent to‘lovi 600 so‘m
Qo‘ng‘iroqlar - 60 daqiqa 📞
Internet - 60 MB 🌐
Cashback - 10 % 🔄

Tarifga ulanish kodi *110*580#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⚪️ Status Silver NEW')
async def bot_start(message: types.Message):
    await message.answer(text="""""⚪️ Status Silver NEW

Oylik abonent to‘lovi 90 000 so‘m
Qo‘ng‘iroqlar - cheksiz 📞
Internet - 20 000 MB 🌐
SMS - 5000 ta ✉️
Roumingda VEON hududi uchun - 250 MB
Bepul «Oltin» raqam - 210 500 so‘m

Tarifga ulanish kodi *110*3#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🟡 Status Gold New')
async def bot_start(message: types.Message):
    await message.answer(text="""""
    🟡  Status Gold NEW

Oylik abonent to‘lovi 130 000 so‘m
Qo‘ng‘iroqlar - cheksiz 📞
Internet - 30 000 MB 🌐
SMS - 10 000 ta ✉️
Roumingda VEON hududi uchun:
 250 MB|| 50 daqiqa || 50% chegirma
Bepul «Oltin» raqam - 421 000 so‘m

Tarifga ulanish kodi *110*2#
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='🔘 Status Platinum New')
async def bot_start(message: types.Message):
    await message.answer(text=""""🔘 Status Platinum NEW

Oylik abonent to‘lovi 189 000 so‘m
Qo‘ng‘iroqlar - cheksiz 📞
Internet - 100 000 MB 🌐
SMS - 10 000 ta ✉️
Roumingda VEON hududi uchun:
 500 MB|| 100 daqiqa || 50% chegirma
Xalqaro Qo‘ng‘iroqlar uchun - 100 daqiqa
Bepul «Oltin» raqam - 421 000 so‘m

Tarifga ulanish kodi *110*1#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='✅ Click +')
async def bot_start(message: types.Message):
    await message.answer(text=""""✅ Click+

Oylik abonent to‘lovi 15 000 so‘m
Internet - 1 GB 🌐
"TAS-IX" - 1 GB 🌐
Ijtimoiy tarmoqlar va 
messsenjerlar uchun- 1 GB 🌐

Tarifga ulanish kodi *10*22#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='💐 Welcome')
async def bot_start(message: types.Message):
    await message.answer(text=""""💐 Welcome

Oylik abonent to‘lovi 30 000 so‘m
Qo‘ng‘iroqlar - 100 📞
Internet - 3000 MB 🌐
Ijtimoiy tarmoqlar va 
messsenjerlar uchun- 1000 MB 🌐
1 ta SMS -  120 so‘m ✉️

Ushbu tarifga ulanish imkoniyati faqat O'zbekistonga kelgan xorijiy sayyohlar uchun  amal qiladi.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='')
async def bot_start(message: types.Message):
    await message.answer(text=""""🎉 G‘alaba!

Qo‘ng‘iroqlar - 300 daqiqa 📞
SMS - 300 ta ✉️\n
Bayram kunlari – 21 mart, 9 may, 1 sentyabr va 31 dekabrda\nabonentlarga Qozog‘iston, Tojikiston, Qirg‘iziston, Turkmaniston va\nRossiyaga xalqaro qo‘ng‘iroqlarni amalga oshirish uchun 7 kunga\nbepul 30 daqiqa ajratiladi. daq/7 kunga
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🧸 Bolajon')
async def bot_start(message: types.Message):
    await message.answer(text=""""🧸 Bolajon

Oylik abonent to‘lovi  11 500 so‘m
Qo‘ng‘iroqlar - 500 daq. tarm. ichida 📞
Qo‘ng‘iroqlar - 125 so‘m daq. tarm. tashqari 📞
SMS - 85 so‘m ✉️
Internet - 1 500 MB 🌐

Tarifga ulanish kodi *110*538#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🆕 Yangi Super hit')
async def bot_start(message: types.Message):
    await message.answer(text=""""🆕 YANGI SUPER XIT

Oylik abonent to‘lovi 33 333 so‘m | 30 000 so‘m(chegirma bn)
Qo‘ng‘iroqlar - 1000 daqiqa 📞
Internet - 4 000 MB 🌐
SMS - 400 ta ✉️

Tarifga ulanish kodi *110*37#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌝 Oylik internet-paketlar')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=oylik_paket)
@dp.message_handler(text='🗓 Haftalik\n'
                            'internet-paketlar')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=hafta_button)
@dp.message_handler(text='🌞 Kunlik\n'
                            'internet-paketlar')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=kun_button)

@dp.message_handler(text='👩‍💻 Kodni aniqlash')

async def bot_start(message: types.Message):
    await message.answer(text="""👩‍💻 Kodni aniqlash

Yangi «Kodni aniqlash» xizmati bilan istagan raqamingizni kodini bilib olasiz!
Buning uchun o’z telefon raqamingizdan *998* abonentning 7 raqami # kodini tersangiz kifoya.
Misol uchun *998*1234567# chaqiruv tugmasi. Xizmat narxi 0 so'm
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📱 Ozmning raqamlarim')

async def bot_start(message: types.Message):
    await message.answer(text="""📱 O‘zimning raqamlarim
Siz bir nechta Beeline raqamlaridan foydalanasiz va ularni qaysi biri sizning nomingizga rasmiylashtirilganligini bilmoqchimisiz?

Yangi «O’zimning raqamlarim» xizmati bilan bu judayam oson va butunlay tekin!

Telefoningizdan *303# tering va javoban Sizning pasport ma'lumotlaringiz bo’yicha ro'yxatdan o'tgan raqamlar ro’yxati, SMS-xabar orqali qabul qilasiz.

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⤴️Boshqa raqamga yonaltirish')

async def bot_start(message: types.Message):
    await message.answer(text="""⤴️ Boshqa raqamga yo’naltirish

Qayta yo'naltirilayotgan mahalliy qo'ng'iroqning 1 daqiqasi narxi 250 so'm/daq.

Barcha qo'ng'iroqlarni yo'naltirish Ulanish **21*operator kodi abonent raqami*11#chaqiruv
Bekor qilish ##21# chaqiruv
Tekshirish uchun *#21# ni tering va chaqiruv tugmasini bosing
Barcha boshqa manzilga yo’llashlarni bekor qilish
##002#chaqiruv
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📓 Qongiroqalar detalizatsiyasi')

async def bot_start(message: types.Message):
    await message.answer(text="""
📋 Qo’ng’iroqlar detalizatsiyasi
Agar Siz hisob-kitobning to’lovdan keyingi tizimida bo’lsangiz, unda Siz qo’ng’iroqlarni detalizatsiyasini bizning Beeline Business ofisimizda yozma ariza, vakilga ishonchnoma taqdim etgach olishingiz mumkin. Vakil amaldagi pasportga ega bo’lishi lozim.
👉 @aloqa_operatorlar_bot""")

@dp.message_handler(text='📲 Qoshimcha sim karta')

async def bot_start(message: types.Message):
    await message.answer(text="""📲 Qo'shimcha SIM-karta 
«Qo'shimcha SIM-karta» xizmati bilan doimo aloqada bo’lishning yangi imkoniyati!
«Qo'shimcha SIM-karta» noyob xizmati abonentlarga SIM-kartalarni almashtirishni ofisdan tashqarida amalga oshirish imkonini beradi.
Xizmatga ulanish narxi 4 210 so'm

👉 BATAFSIL MA'LUMOT (https://beeline.uz/uz/products/services/zapasnaya-sim-karta.html)

Qo'shimcha SIM-karta
«Qo'shimcha SIM-karta» xizmati bilan doimo aloqada bo’lishning yangi imkoniyati! «Qo'shimcha SIM-karta» noyob xizmati abonentlarga SIM-kartalarni almashtirishni ofisdan tashqar
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='💰 Hisobimni toldirib qoy')
async def bot_start(message: types.Message):
    await message.answer(text="""💰 hisobimni to‘ldirib qo‘y 
Hisobingizni to’ldirish haqidagi iltimosingizni nafaqat O’zbekistondagi qarindosh va yaqinlaringizga, balki Rossiya va Qozog'istonda yashovchilarga ham yuboring!

Kuniga bepul so’rovlar soni 5 SMS
6 so’rovdan boshlab xizmat narxi 42.1 so'm
*143*Davlat kodi Operator kodi Telefon raqam# 

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🤙 Menga qongiroq qil')
async def bot_start(message: types.Message):
    await message.answer(text="""🤙 Menga qo‘ng‘iroq qil
Hisobingizda yetarlicha pul bo'lmaganda, endi Sizga qachon yaqinlaringiz qo'ng'iroq qilishar ekan deb kutish shart emas. «Menga qo'ng'iroq qil» xizmati yordamida siz bitta so’rov bilan abonentning qo'ng'irog’ini kutayotganingiz haqida xabar berishingiz mumkin.

Kuniga bepul so’rovlar soni 5 SMS
6 so’rovdan boshlab xizmat narxi 42.1 so'm
*145*Davlat kodi Operator kodi Telefon raqam # chaqiruv tugmasi 

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='0️⃣ Jonli nol')
async def bot_start(message: types.Message):
    await message.answer(text="""0️⃣ Jonli nol 
Hisobingizdagi pul tugab qoldimi? Muhim qo’ng’iroqni o’tkazib yuborishdan xavotirga tushmang: avvaldan to’lov tizimidagi barcha abonentlarda balansdagi nol “jonli”!

O’z uyali telefoningizni o’chirmang – va yaqinlaringiz sizga hamisha qo’ng’iroq qila oladi!

👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📞 Beep call')
async def bot_start(message: types.Message):
    await message.answer(text="""📞 Beep Call 
BeepCall - bepul xizmat bo'lib, turli hayotiy vaziyatlarda abonentlarga qulaylik yaratish maqsadida yaratilgan.

👉 BATAFSIL MA'LUMOT (https://beeline.uz/uz/products/services/beep-call.html)
👉 @aloqa_operatorlar_bot

beeline.uz (https://beeline.uz/uz/products/services/beep-call.html)
Beep Call
BeepCall - bepul xizmat bo'lib, turli hayotiy vaziyatlarda abonentlarga qulaylik yaratish maqsadida yaratilgan. 

""")
@dp.message_handler(text='🔓 Raqamni blokirovka qilish')
async def bot_start(message: types.Message):
    await message.answer(text=""""🔒 Raqamni blokirovka qilish 
Xizmat abonentning xohishiga ko’ra raqamni blokirovka qilish imkoniyatini beradi.

Oldindan to'lov tizimi tariflardagi abonentlar uchun xizmatga ulanish narxi 421 so'm

👉 BATAFSIL MA'LUMOT (https://beeline.uz/uz/products/services/blokirovka_nomera.html)
👉 @aloqa_operatorlar_bot

beeline.uz (https://beeline.uz/uz/products/services/blokirovka_nomera.html)
Abonentning xohishiga ko’ra raqamni blokirovka qilish
Xizmat abonentning xohishiga ko’ra raqamni blokirovka qilish imkoniyatini beradi. 

""")
@dp.message_handler(text='<-<Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text="""Ortga qaytdingiz""",reply_markup=boshqa_hizmatlar_button)
