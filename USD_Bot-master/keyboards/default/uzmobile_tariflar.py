from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


uzmobile_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📓 Street'),
            KeyboardButton(text='📔 Flash'),
            KeyboardButton(text='📒 Royal')
        ],
        [
            KeyboardButton(text='📕 Ishbilarmon'),
            KeyboardButton(text='📘 Oddiy 10'),
            KeyboardButton(text='📗 Onlime')
        ],
        [
            KeyboardButton(text='📙 Yoshlar'),
            KeyboardButton(text="🎓 Ta'lim"),
            KeyboardButton(text='📚 Maktab')
        ],
        [
            KeyboardButton(text='🚀 Street Upgrade'),
            KeyboardButton(text='✈️ Flash Upgrade')
        ],
        [
            KeyboardButton(text='👼 Bolajon'),
            KeyboardButton(text='⬅️ Orqaga')
        ]
    ],resize_keyboard=True
)
uzmobile_internet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔰 Oylik internet'),
            KeyboardButton(text='♻️ Internet non-stop')
        ],
        [
            KeyboardButton(text='🗓 TAS-IX uchun Internet'),
            KeyboardButton(text='🌞 Kunlik Internet')
        ],
        [
            KeyboardButton(text='⬅️ Orqaga')
        ]
    ],resize_keyboard=True
)
oylik_internet_uzmobie = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔰 1000 MB'),
            KeyboardButton(text='🔰 1500 MB'),
            KeyboardButton(text='🔰 3000 MB')
        ],
        [
            KeyboardButton(text='🔰 5000 MB'),
            KeyboardButton(text='🔰 8000 MB'),
            KeyboardButton(text='🔰 12000 MB')
        ],
        [
            KeyboardButton(text='🔰 12000 MB'),
            KeyboardButton(text='🔰 20000 MB'),
            KeyboardButton(text='🔰 30000 MB')
        ],
        [
            KeyboardButton(text='🔰 50000 MB'),
            KeyboardButton(text='🔰 75000 MB'),
            KeyboardButton(text='🔙 Orqaga')
        ],
    ],resize_keyboard=True
)
non_stop_internet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='♻️ 3 000 MB non-stop'),
            KeyboardButton(text='♻️ 5 000 MB non-stop')
        ],
        [
            KeyboardButton(text='♻️ 8 000 MB non-stop'),
            KeyboardButton(text='♻️ 12 000 MB non-stop')
        ],
        [
            KeyboardButton(text='♻️ 20 000 MB non-stop'),
            KeyboardButton(text='♻️ 30 000 MB non-stop')
        ],
        [
            KeyboardButton(text='♻️ 50 000 MB non-stop'),
            KeyboardButton(text='🔙 Orqaga')
        ]
    ],resize_keyboard=True
)
tas_ix_internet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 TAS-IX 2 048'),
            KeyboardButton(text='🗓 TAS-IX 10 240')
        ],
        [
            KeyboardButton(text='🗓 TAS-IX 15 360'),
            KeyboardButton(text='🔙 Orqaga')
        ]
    ],resize_keyboard=True
)
kunlik_internet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌞 100 MB'),
            KeyboardButton(text='🌞 300 MB')
        ],
        [
            KeyboardButton(text='🌞 600 MB'),
            KeyboardButton(text='🔙 Orqaga')
        ]
    ],resize_keyboard=True
)
uzmobile_boshqa_hizmat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Asosiy xizmatlar'),
            KeyboardButton(text='☑️ Qo‘shimcha xizmatlar')
        ],
        [
            KeyboardButton(text='📩SMS xizmatlar'),
            KeyboardButton(text='⬅️ Orqaga')
        ]
    ],resize_keyboard=True
)
boshqa_hizmat_asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗣 Ovozli pochta'),
            KeyboardButton(text='👁 Yashirin qo‘ng‘iroq')
        ],
        [
            KeyboardButton(text='↗️ Qo‘ng‘iroqni boshqa raqamga yo‘naltirish'),
        ],
        [
            KeyboardButton(text='❌ Shaxsiy raqam uzatilishini taqiqlash')
        ],
        [
            KeyboardButton(text='⏳ Chaqiruvni kutish'),
            KeyboardButton(text='🔙  Orqaga')
        ]
    ],resize_keyboard=True
)
boshqa_hizmat_qoshimcha = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔄 Foydali almashinuv'),
            KeyboardButton(text='🔊 «Limitsiz ovoz»')
        ],
        [
            KeyboardButton(text='🤝 Qo‘llab yubor'),
            KeyboardButton(text='🌌 Tungi Internet')
        ],
        [
            KeyboardButton(text='💰 EXTRA balans'),
            KeyboardButton(text='☎️ Tungi qo’ng’iroqlar')
        ],
        [
            KeyboardButton(text='♻️ Restart'),
            KeyboardButton(text='📚 «ZiyoNET»'),
            KeyboardButton(text='👨‍👩‍👧 «Oila uchun»')
        ],
        [
            KeyboardButton(text='🧾 YHQ jarimalari haqida xabar')
        ],
        [
            KeyboardButton(text='🔁 Tezkor o‘tkazmalar'),
            KeyboardButton(text='♥️ Sevimli raqamlar')
        ],
        [
            KeyboardButton(text='⚠️ «Qabul qilinmagan qo‘ng‘iroq» va «Tarmoqda»'),
            KeyboardButton(text='🔙  Orqaga')
        ]
    ],resize_keyboard=True
)
boshqa_hizmat_sms1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📩 Oylik SMS-paketlar'),
            KeyboardButton(text='✉️ Har kunlik SMS'),
        ],
        [
            KeyboardButton(text='📨 Xalqaro SMS-paketlar'),
            KeyboardButton(text='🔙  Orqaga')
        ]
    ],resize_keyboard=True
)
oylik_sms_paketlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📩 MS 10 SMS'),
            KeyboardButton(text='📩 MS 50 SMS'),
        ],
        [
            KeyboardButton(text='📩 MS 200 SMS'),
            KeyboardButton(text='📩 MS 500 SMS'),
        ],
        [
            KeyboardButton(text='◀️ Orqaga')
        ]
    ],resize_keyboard=True
)
kunlik_sms = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✉️ 50 SMS Daily'),
            KeyboardButton(text='✉️ 100 SMS Daily')
        ],
        [
            KeyboardButton(text='◀️ Orqaga')
        ]
    ],resize_keyboard=True
)
xalqaro_sms = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📨 MS 10 MN SMS'),
            KeyboardButton(text='📨 MS 20 MN SMS')
        ],
        [
            KeyboardButton(text='📨 MS 30 MN SMS'),
            KeyboardButton(text='📨 MS 40 MN SMS')
        ],
        [
            KeyboardButton(text='📨 MS 50 MN SMS'),
            KeyboardButton(text='◀️ Orqaga')
        ],
    ],resize_keyboard=True
)
