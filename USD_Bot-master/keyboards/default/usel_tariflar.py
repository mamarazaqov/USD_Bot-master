from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


cosmo_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛰 Cosmo 16'),
            KeyboardButton(text='🛰 Cosmo 23')
        ],
        [
            KeyboardButton(text='🛰 Cosmo 28'),
            KeyboardButton(text='<<<Orqaga')
        ]
    ],resize_keyboard=True
)
special_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📗 Special 35'),
            KeyboardButton(text='📗 Special 45')
        ],
        [
            KeyboardButton(text='📗 Special 55'),
            KeyboardButton(text='📗 Special 70')
        ],
        [
            KeyboardButton(text='📗 Special 80'),
            KeyboardButton(text='📗 Special 100')
        ],
        [
            KeyboardButton(text='📗 Special Unlim'),
            KeyboardButton(text='📗 Special Unlim Turbo')
        ],
        [
            KeyboardButton(text='<<<Orqaga')
        ]
    ],resize_keyboard=True
)
special_plus_tariflar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📗 Special 35➕'),
            KeyboardButton(text='📗 Special 55➕')
        ],
        [
            KeyboardButton(text='📗 Special 80➕'),
            KeyboardButton(text='📗 Special 125➕')
        ],
        [
            KeyboardButton(text='<<<Orqaga')
        ]
    ],resize_keyboard=True
)
kayfiyat_tariflar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎭 Yaxshi kayfiyat'),
            KeyboardButton(text="🎭 Zo'r kayfiyat")
        ],
        [
            KeyboardButton(text="🎭 A'lo kayfiyat"),
            KeyboardButton(text='<<<Orqaga')
        ]
    ],resize_keyboard=True
)
tantana_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎉 Tantana'),
            KeyboardButton(text='🎉 Katta tantana')
        ],
        [
            KeyboardButton(text='🎉 Super tantana'),
            KeyboardButton(text='<<<Orqaga')
        ]
    ],resize_keyboard=True
)
internet_hizmat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Oylik Internet to‘plamlari'),
        ],
        [
            KeyboardButton(text='📆 Haftalik Internet-to‘plamlar'),
            KeyboardButton(text='☀️ Kunlik Internet-to‘plamlar')
        ],
        [
            KeyboardButton(text='➡️Internet-o‘tkazma'),
            KeyboardButton(text='💃 Aksiya: 1gb, 2gb, va 3gb')
        ],
        [
            KeyboardButton(text='⏳ Soatbay internet'),
            KeyboardButton(text='🌙 Tungi internet-to‘plamlar')
        ],
        [
            KeyboardButton(text='♾ Cheksiz Internet-to‘plamlar'),
            KeyboardButton(text='✈️ Oylik 4G Internet-to‘plamlar')
        ],
        [
            KeyboardButton(text='📡 TAS-IX uchun internet-to‘plamlar'),
            KeyboardButton(text='🎁 Internet-sovg‘a')
        ],
        [
            KeyboardButton(text='💥 Mega BOOM'),
            KeyboardButton(text='💵 Internet-avans')
        ],
        [
            KeyboardButton(text='<<Orqaga')
        ]
    ]
)
