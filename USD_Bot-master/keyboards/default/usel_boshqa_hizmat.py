from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


boshqa_hizmat_usel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✳️ «U+» sodiqlik dasturi!'),
            KeyboardButton(text='🎊 «Navro‘z 2021» xizmati')
        ],
        [
            KeyboardButton(text='☎️ Mening raqamlarim'),
            KeyboardButton(text='🔗 «Yagona hisob»')
        ],
        [
            KeyboardButton(text='👁‍🗨 Raqamni yashirish'),
            KeyboardButton(text="⚙️ Qo'ng'iroqlar filtri")
        ],
        [
            KeyboardButton(text='🇷🇸🇺🇿🇺🇸 Tilni tanlash'),
            KeyboardButton(text='📞 Maxfiy qo‘ng‘iroq xizmati')
        ],
        [
            KeyboardButton(text='↩️ O‘tkazib yuborilgan qo‘ng‘iroqlar')
        ],
        [
            KeyboardButton(text="📱📲 Mobil o'tkazma"),
            KeyboardButton(text='💵 Mobil avans')
        ],
        [
            KeyboardButton(text="✉️ SMS-To'plamlar"),
            KeyboardButton(text='📝 SMS Taxallus')
        ],
        [
            KeyboardButton(text='⚫️ SMS Filtr-Qora ro‘yxat'),
            KeyboardButton(text='🔑 "Mening kabinetim"')
        ],
        [
            KeyboardButton(text='🌐 "Butun dunyo" xizmati'),
            KeyboardButton(text='📩 Xalqaro SMS-to’plamlar')
        ],
        [
            KeyboardButton(text='🎧 Ucell Operatori bilan bog‘lanish')
        ],
        [
            KeyboardButton(text='<<Orqaga')
        ]
    ],resize_keyboard=True
)