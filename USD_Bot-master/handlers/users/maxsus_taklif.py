from aiogram import types
from keyboards.default.qoshimcha_hizmat import *
from loader import dp


@dp.message_handler(text='🧾 Maxsus takliflar')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang",reply_markup=maxsus_taklif_button)
@dp.message_handler(text='📺 Beeline TV')
async def bot_start(message: types.Message):
    await message.answer(text="""📺 Beeline TV
Internetingizni sarflamay sevimli filmlar va seriallarni tomosha qiling!

TV (kunlik obuna) 599 so'm/kun
IVI (kunlik obuna) 799 so'm/kun
Milliy (kunlik obuna) 699 so'm/kun
Megogo (kunlik obuna) 799 so'm/kun
Start (kunlik obuna) 799 so'm/kun
GOLD (TV, IVI, Milliy) (kunlik obuna) 1 499 so'm/kun
VIP (TV, IVI, Start, Milliy) (kunlik obuna) 1 999 so'm/kun

⬇️ Yuklash (http://onelink.to/2k3hg5)
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🎼 Beeline Music & Radio')
async def bot_start(message: types.Message):
    await message.answer(text="""🎼 Beeline Music & Radio
Internet trafikni sarflamagan holda sevimli musiqangizni tinglashdan bahramand bo'ling!

Kunlik obuna 599 so'm/kun
Oylik obuna 14 999 so'm/oy
⬇️ Yuklash (https://bit.ly/beemus-i)

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='⚽️ Fantasy Football')
async def bot_start(message: types.Message):
    await message.answer(text="""⚽️ Fantasy Football
899 so'm/kun yoki 17999 so'm/oy evaziga haqiqiy futbolchilardan tashkil topgan «FANTASTIK JAMOANGIZNI» YARATING.
SAYTGA O‘TISH (http://lp.fantasy.beeline.uz/landing?utm_source=beeline_website)

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🛠 Beeline App')
async def bot_start(message: types.Message):
    await message.answer(text="""🛠 Beeline App
Reklamasiz va trafikni sarflamagan holda eng zo'r o'yinlar va mobil ilovalarni yuklab oling!

Kunlik obuna 1 299 so'm/kun
Oylik obuna 24 999 so'm/oy

SAYTGA O‘TISH (http://app.beeline.uz/store/buy?utm_source=beeline_site)

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🗞 Beeline Pressa')
async def bot_start(message: types.Message):
    await message.answer(text="""🗞 Beeline Pressa
Internet trafikni sarflamagan holda sevimli jurnallar va gazetalaringizni onlayn rejimida o'qing!

Kunlik obuna 499 so'm/kun
SAYTGA O‘TISH (https://pressa.beeline.uz/)
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='📚 Bookmate')
async def bot_start(message: types.Message):
    await message.answer(text="""📚 Bookmate
Internet trafikni sarflamagan holda sevimli kitoblaringizni o'qing va tinglang!

Kunlik obuna 599 so'm/kun
⬇️ Yuklash (http://bit.ly/books_bee)
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🎶 Yandex.Musiqa')
async def bot_start(message: types.Message):
    await message.answer(text="""🎶 "Yandex.Musiqa"ni tinglang va internet trafik haqida qayg'urmang!

Kunlik obuna 499 so'm/kun
Oylik obuna 14 999 so'm/oy
⬇️ Yuklash (http://onelink.to/eft3vy)
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🏃 Qadamlar uchun Giglar')
async def bot_start(message: types.Message):
    await message.answer(text="""🏃 Qadamlar uchun Giglar
Sizdan qadamlar-bizdan gigabaytlar! Beeline bilan birga qadam bosing!

⬇️ Yuklash (http://bit.ly/AppBeeline) 
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text='🔄 Perezagruzka')
async def bot_start(message: types.Message):
    await message.answer(text="""🔄 Perezagruzka 

Agarda Sizda tarif rejangiz bo’yicha taqdim etilgan trafik yakunlansa, unda Siz ushbu xizmatdan foydalanib, tarif rejani qayta ishga tushirib, daqiqa, SMS va MB paketlarini to'liq hajmda olishingiz mumkin.
Ulanish kodi: *5#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="💳 Ishonchli to'lov")
async def bot_start(message: types.Message):
    await message.answer(text="""💳 Ishonchli to'lov

Sizning so’rovingizga binoan, Beeline hisobingizdagi mablag'ni vaqtincha ko'paytiradi va siz aloqada bo'lasiz!
Xizmat narxi - taqdim etilgan mablag' miqdorining % ni tashkil etadi 15 %
Ulanish kodi: *141#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="☎️ Oltin raqamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""☎️ Oltin raqamlar

Boshqalardan ajralib turishni istaysizmi? U holda "Beeline" dan oltin raqam tanlang!
Raqam niqobi O'zbekiston abonentlari uchun amal qiladi.
Boshlang'ich narxi 50 000 so'm

BATAFSIL (https://beeline.uz/uz/products/services/zolotie-nomera.html)
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🌀 Xabardor bo‘l")
async def bot_start(message: types.Message):
    await message.answer(text="""🌀 Xabardor bo‘l

Agar sizning telefoningiz eng kerak vaqtda o’chib qolsa, siz biror  bir qo'ng'iroqni o'tkazib yubormaysiz.  
Sizga qo'ng'iroq qilishgan raqamlari SMS-xabar orqali keladi.
Ulanish kodi: *110*051# Xizmat bepul
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🤝 Bog‘lanish mumkin")
async def bot_start(message: types.Message):
    await message.answer(text="""🤝 Bog‘lanish mumkin
Sizga qo’ng’iroq qilgan abonentlar hamisha sizning telefoningiz tarmoqda paydo bo’lganligidan va siz bilan yana aloqa bog’lash mumkinligidan xabardor qilinadi.
Xizmat bepul Ulanish kodi: *110*051#

👉 @aloqa_operatorlar_bot
""")

@dp.message_handler(text="🙅‍♂️ Sirli qo’ng’iroq")
async def bot_start(message: types.Message):
    await message.answer(text="""🙅‍♂️ Sirli qo’ng’iroq 
Endi istagan paytingizda qo'ng'iroq qilayotganingizda o'z raqamingizni yashirib qo'ng'iroq qilishingiz mumkin!
Xizmat narxi 252.6 so'm/daq.
M: #99890ХХХХХХХ
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🎵Mening musiqam")
async def bot_start(message: types.Message):
    await message.answer(text="""🎵Mening musiqam
«Mening musiqam» – abonentga kiruvchi qo’ng’iroqlar uchun odatdagi chaqiruv gudoklari o’rniga har xil ohanglar va tovushlar o’rnatish imkoniyatini taqdim etadi.
Abonent to’lovi 210.5 so'm/kun
Ulanish kodi: *110*311#
👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="🧐 Raqamni antianiqlash")
async def bot_start(message: types.Message):
    await message.answer(text="""🧐 Raqamni antianiqlash

Qo’ng’iroq chog’ida Antianiqlash sizning raqamingizni, hatto suhbatdoshda Raqamni aniqlash xizmati o’rnatilgan taqdirda ham, sir saqlaydi.
Xizmatga ulanish narxi 421 so'm
Kunlik abonent to`lovi 421 so'm/kun
II turdagi antianiqlash - *110*071#
III turdagi antianiqlash - *110*072#

👉 @aloqa_operatorlar_bot
""")
@dp.message_handler(text="✔️ Raqam tanlash va band qilish")
async def bot_start(message: types.Message):
    await message.answer(text="""✔️ Raqam tanlash va band qilish
ndi raqamni uydan chiqmasdan tanlash mumkin!
"Raqam tanlash va band qilish" xizmati yordamida siz nomer.beeline.uz saytida ko'rsatilgan raqamlardan o'zingizga yoqqan raqamni tanlab, band qilib, o'zingizga qulay Beeline ofislaridan birida ulanishingiz mumkin.

 nomer.beeline.uz  (http://nomer.beeline.uz/)
👉 @aloqa_operatorlar_bot
""")