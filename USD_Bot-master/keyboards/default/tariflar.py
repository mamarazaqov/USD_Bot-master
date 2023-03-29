from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
tariflar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👍 ZO'R 2"),
            KeyboardButton(text="👍 ZO'R 6"),
            KeyboardButton(text="👍 ZO'R 10")
        ],
        [
            KeyboardButton(text="👍 ZO'R 15"),
            KeyboardButton(text="📞 ALLO"),
            KeyboardButton(text="📅 Kunlik")
        ],
        [
            KeyboardButton(text='⚪️ Status Silver NEW'),
            KeyboardButton(text='🟡 Status Gold New')
        ],
        [
            KeyboardButton(text='🔘 Status Platinum New'),
            KeyboardButton(text='✅ Click +')
        ],
        [
            KeyboardButton(text='💐 Welcome'),
            KeyboardButton(text='🏆 Galaba')
        ],
        [
            KeyboardButton(text='🧸 Bolajon'),
            KeyboardButton(text='🆕 Yangi Super hit')
        ],
        [
            KeyboardButton(text='🏠 Bosh menu'),
            KeyboardButton(text='<-Orqaga')
        ]
    ],resize_keyboard=True
)
internet_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌝 Oylik internet-paketlar')
        ],
        [
            KeyboardButton(text='🗓 Haftalik\n'
                                'internet-paketlar'),
            KeyboardButton(text='🌞 Kunlik\n'
                                'internet-paketlar')
        ],
        [
            KeyboardButton(text='🚀 4G Internet-paketlar'),
            KeyboardButton(text='<- Orqaga')
        ]
    ],resize_keyboard=True
)
boshqa_hizmatlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔰 Asosiy xizmatlar'),
            KeyboardButton(text='🌐 Internet hizmatlar')
        ],
        [
            KeyboardButton(text='📩 SMS xizmatlar'),
            KeyboardButton(text='📩 Xalqaro SMS')
        ],
        [
            KeyboardButton(text='🧾 Maxsus takliflar'),
            KeyboardButton(text='<- Orqaga')
        ]
    ],resize_keyboard=True
)

usel_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚀 Cosmo tariflari'),
            KeyboardButton(text='📲 Special tariflari')
        ],
        [
            KeyboardButton(text='➕ Special+ tariflari'),
            KeyboardButton(text='🎭 Kayfiyat tariflari')
        ],
        [
            KeyboardButton(text='🎉 Tantana tariflari'),
            KeyboardButton(text='🏨 Marhamat tarifi')
        ],
        [
            KeyboardButton(text='📆 Yengil hafta'),
            KeyboardButton(text='🎓 Student')
        ],
        [
            KeyboardButton(text='💼️ Oddiy'),
            KeyboardButton(text='✈️ Uchar internet')
        ],
        [
            KeyboardButton(text='<<Orqaga')
        ]
    ]
)
