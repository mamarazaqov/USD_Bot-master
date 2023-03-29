from aiogram import types
from keyboards.default.tariflar import *
from keyboards.default.usel_boshqa_hizmat import *
from loader import dp


@dp.message_handler(text='💬 Boshqa xizmatlar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=boshqa_hizmat_usel)
@dp.message_handler(text='✳️ «U+» sodiqlik dasturi!')
async def bot_start(message: types.Message):
    await message.answer(text="""✳️ «U+» sodiqlik dasturi!:

16.02.2021-y.dan «Cosmo» va «Special» tariflari tizimi abonentlari abonent to‘lovini amalga oshirganda abonent to‘lovi miqdorining 5% qismini promo hisobga keshbek shaklida olishlari mumkin. To‘plangan promo birliklarni tegishli tarif rejalari abonentlari quyidagi takliflarga almashtirishlari mumkin bo‘ladi:

1. 1 yilga cheksiz Telegram
2. 1 yilga O‘zbekiston bo‘yicha cheksiz qo‘ng‘iroqlar
3. 1 yilga cheksiz YouTube
4. 1 yilga cheksiz ijtimoiy tarmoqlar (Facebook, Instagram, OK, VKontakte)
5. 1 yilga cheksiz Tas-IX

«U+» sodiqlik dasturining shartlari faqat «COSMO 16», «COSMO 23», «COSMO 28», «Special 35», «Special 45», «Special 55», «Special 70», «Special 80», «Special 100» va «Special 125» tarif rejalari abonentlari, shuningdek, «Kuzgi syurpriz» aksiyasi doirasida ulangan abonentlar uchun amal qiladi.
«U+» dasturida ishtirok etish uchun *470# USSD-so‘rovi yordamida ro‘yxatdan o‘tish lozim.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🎊 «Navro‘z 2021» xizmati')
async def bot_start(message: types.Message):
    await message.answer(text="""🎊 «Navro‘z 2021» xizmati:

Navro‘z 2021” xizmatidan foydalanib, atigi 2021 so‘mga 2021 MB, O‘zbekiston bo‘yicha 2021 daqiqa va 2021 SMS oling.
Limitlarni tekshirish *620#
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='☎️ Mening raqamlarim')
async def bot_start(message: types.Message):
    await message.answer(text="""☎️ Mening raqamlarim":

O‘zingizning pasportingizga qaysi raqamlar rasmiylashtirilganligini unutib qo‘ydingizmi? Ucell Sizga o‘z raqamlaringiz haqida, shu jumladan ularning holati, hisobi va faol pulli xizmatlar xususida batafsil ma’lumotlarni olishga yordam beradi!
Xizmatdan foydalanish: *️⃣3️⃣6️⃣0️⃣#️⃣ 
So‘rovlar miqdori cheklangan – kuniga 2 so‘rov..
Xizmat bepul.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔗 «Yagona hisob»')
async def bot_start(message: types.Message):
    await message.answer(text="""🔗 «Yagona hisob» :

Har bir xizmat bo‘yicha hisobni tekshirish uchun ko‘plab USSD-so‘rovlarni eslab yurishdan charchadingizmi?
«Yagona hisob» xizmati abonentlarga raqamning tarif rejasi va ulangan barcha xizmatlar doirasidagi limitlar qoldiqlari haqida ma’lumot olish imkonini beradi.
Ma’lumotni  *️⃣9️⃣0️⃣0️⃣#️⃣so‘rovini yuborib olish mumkin
Xizmat bepul.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='👁‍🗨 Raqamni yashirish')
async def bot_start(message: types.Message):
    await message.answer(text="""👁‍🗨 Raqamni yashirish:

Ucell abonentlari uchun ushbu xizmat qo‘ng‘iroq vaqtida shaxsiy raqamlarini qo‘ng‘iroq qilayotgan abonentning mobil telefoni displeyida ko‘rinmaslik imkoniyatini beradi. Qo‘ng‘roq qilayotgan abonentning mobil telefoni displeyida "Raqam aniqlanmagan" yoki telefon apparati sozlashlariga hos boshqa ma’lumot ko‘rinadi.
Xizmatni boshqarish: *️⃣3️⃣1️⃣1️⃣#️⃣
Abonent to'lovi - 421 so‘m/ kuniga (abonent to'lovi xizmat faollashtirilgandang so'ng yechiladi)
30 kunlik “Raqamni yashirish”
Siz “Raqamni yashirish” xizmatining juda qulay va hamyonbop opsiyasidan foydalanishingiz mumkin. Bir marta to‘lab, 30 kun foydalaning.
Narxi – 30 kunga 6990 so‘m. Faollashtirish: *321#.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="⚙️ Qo'ng'iroqlar filtri")
async def bot_start(message: types.Message):
    await message.answer(text="""⚙️ Qo'ng'iroqlar filtri:


"Qo‘ng‘iroqlar filtri" xizmati Qora ro‘yxatga kiritilgan raqamlardan kelayotgan qo‘ng‘iroqlarni bloklash yoki O‘q ro‘yxatga kiritilgan raqamlardan boshqa barcha raqamlarni bloklash imkoniyatini beradi.
Agar bloklangan abonent sizga qo‘ng‘iroq qilishga urunsa u "Chaqirilayotgan abonent hozir javob bera olmaydi" degan xabarni oladi.
Oddiy rejasini ishga tushirish: *️⃣9️⃣8️⃣8️⃣*️⃣1️⃣#️⃣
Biznes rejasini ishga tushirish: *️⃣9️⃣8️⃣8️⃣*️⃣2️⃣#️⃣
Oddiy rejasining narxi - 336.8 so‘m kuniga.
Biznes rejasining narxi - 842 so‘m kuniga.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🇷🇸🇺🇿🇺🇸 Tilni tanlash')
async def bot_start(message: types.Message):
    await message.answer(text="""🇷🇸🇺🇿🇺🇸 "Tilni tanlash" xizmati:

Endi siz USSD va SMS habarlarning qabul qilish tilini o‘zingiz tanlashingiz mumkin.
O‘z tilingizni tanlash uchun *220# raqamiga USSD so‘rov yuboring. So‘rov yuborilgandan so‘ng sizga quyidagi amallarni bajarish taklif etiladi:
Hozirgi vaqtda sizda o‘rnatilgan tilni tanlash uchun – 1 raqami bilan javob qaytaring;
Habarlar tilini almashtirish uchun – 2 raqami bilan javob qaytaring.
Xizmat BEPUL taqdim etiladi.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📞 Maxfiy qo‘ng‘iroq xizmati')
async def bot_start(message: types.Message):
    await message.answer(text="""📞 Maxfiy qo‘ng‘iroq xizmati:

Ucell abonentlarga yangi “Maxfiy qo‘ng‘iroq” xizmatini taqdim etadi. Endi siz “Raqamni yashirish” xizmatini faollashtirilmagan holda raqamingizni yashirib qo‘ng‘iroq qilish imkoniayiga egasiz.
Buning uchun “9*” (9 raqami va "*" belgisini) abonent raqami oldidan terishingiz lozim: 9*998YYххххххх
Narxi - 252.6 so‘m/daqiqa.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='↩️ O‘tkazib yuborilgan qo‘ng‘iroqlar')
async def bot_start(message: types.Message):
    await message.answer(text="""↩️ O‘tkazib yuborilgan qo‘ng‘iroqlar xizmatlari:

Sizga kim qo‘ng‘iroq qilganidan boxabar bo‘ling!
*977# raqamiga USSD-so‘rov yuborib, o‘tkazib yuborilgan qo‘ng‘iroqlar haqida qay tartibda xabar topishni o‘zingiz tanlang!
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="📱📲 Mobil o'tkazma")
async def bot_start(message: types.Message):
    await message.answer(text="""📱📲 Mobil o'tkazma:

Xizmatdan foydalanish uchun: *650#
Mablag‘ yuborish yoki qabul qilish ushun xizmatni ulash kerak emas.
168.4 so‘m  bitta muvaffaqiyatli pul o‘tkazishning narxi  (mablag‘ pul o‘tkazuvchi-abonent hisobidan ushlab qolinadi).
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='💵 Mobil avans')
async def bot_start(message: types.Message):
    await message.answer(text="""💵 Mobil avans:

Hisobda pul tugab, hisobni to‘ldirish imkoni bo‘lmasa ham "Mobil avans" xizmati bilan siz doimo aloqada bo‘lasiz.

21050 so‘m. Xizmat haqi 2105 so‘m.
12630 so‘m. Xizmat haqi 1263 so‘m.
4210 so‘m. Xizmat haqi 842 so‘m.
2105 so‘m. Xizmat haqi 421 so‘m.

Xizmatdan foydalanish uchun  *️⃣9️⃣1️⃣1️⃣#️⃣raqamiga USSD so‘rov yuboring.
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text="✉️ SMS-To'plamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""✉️ SMS-To'plamlar:

SMS-To‘plam 50. Narxi: 1 684 so‘m
SMS-To‘plam 150. Narxi: 4 210 so‘m
SMS-To‘plam 500. Narxi: 10 525 so‘m

Xizmatni boshqarish: *️⃣1️⃣4️⃣7️⃣#️⃣
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📝 SMS Taxallus')
async def bot_start(message: types.Message):
    await message.answer(text="""📝 SMS Taxallus:

Xizmatni boshqarish - *️⃣3️⃣2️⃣7️⃣#️⃣
Chiquvchi SMS xabarining narxi – 84.2 so‘m (amaldagi chiqish SMS narxiga qoʻshimcha sifatida va abonent tarif rejasidan qat’iy nazar)
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='⚫️ SMS Filtr-Qora ro‘yxat')
async def bot_start(message: types.Message):
    await message.answer(text="""⚫️ SMS Filtr-Qora ro‘yxat:

"SMS Filtr-Qora ro‘yxat" xizmati Qora ro‘yxatga kiritilgan Ucell abonentlari raqamlaridan kiruvchi SMS xabarlarni taqiqlash imkoniyatini beradi.
Xizmat narxi - kuniga 210.5 so‘m
Xizmatni boshqarish:*️⃣3️⃣2️⃣4️⃣#️⃣ 
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🔑 "Mening kabinetim"')
async def bot_start(message: types.Message):
    await message.answer(text="""🔑 "Mening kabinetim":

Prepaid abonentlar uchun imkoniyatlar:
tarif rejasini almashtirish;
qo‘ng‘iroqlarning va taqdim etilgan xizmatlar uchun mablag‘lar yechilishining batafsil tarixini ko‘rish;
SMS-xabarlar yuborish;
Kompaniyaning abonentlar bo‘limiga murojaat yuborish.
Shaxsiy kabinetda ro‘yxatdan o‘tish:
Tizimda ro‘yxatdan o‘tish uchun abonent o‘z telefon raqamini va bir martalik parolni ko‘rsatishi lozim.

 Bir martalik parol – parolni olish uchun abonent ko‘rsatilgan telefon raqamidan *️⃣2️⃣3️⃣3️⃣#️⃣ terishi va olingan parolni tegishli joyga kiritishi lozim.
 Mening kabinetimga kirish: my.ucell.uz 
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🌐 "Butun dunyo" xizmati')
async def bot_start(message: types.Message):
    await message.answer(text="""🌐 "Butun dunyo" xizmati:

Xalqaro qo‘ng‘iroqlarga taklif!
"Butun Dunyo" xizmatini faollashtiring va MDH davlatlariga (Qozog'iston, Tojikiston, Turkmaniston, Qirg'iziston, Rossiya, Ukraina, Belarus, Moldova, Armaniston, Gruziya va Ozarbayjon)daqiqasiga atigi 1500 so‘mga muloqot qiling, dunyoning istalgan boshqa davlati bilan esa daqiqasiga 5000 so‘mga.
Xizmatga ulanish narxi atigi 500 so‘m.
Abonent to‘lovi – kuniga 100 so‘m
Xizmatni boshqarish: *️⃣1️⃣5️⃣0️⃣*️⃣1️⃣#️⃣
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='📩 Xalqaro SMS-to’plamlar')
async def bot_start(message: types.Message):
    await message.answer(text="""📩 Xalqaro SMS-to’plamlar:

10 SMS 8 000 UZS Xarid qilish 30 kun
30 SMS 22 000 UZS Xarid qilish    30 kun
50 SMS 34 000 UZS Xarid qilish    30 kun
100 SMS 64 000 UZS Xarid qilish    30 kun

Xizmatni boshqarish: *️⃣7️⃣8️⃣9️⃣#️⃣
👉 @aloqa_operatorlar_bot""")
@dp.message_handler(text='🎧 Ucell Operatori bilan bog‘lanish')
async def bot_start(message: types.Message):
    await message.answer(text="""🎧 Ucell Operatori bilan bog‘lanish:

Call Center: +998 93 180 00 00
Qisqa raqam: 8123 
👉 @aloqa_operatorlar_bot""")