from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
oylik_paket =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌛 Internet paket-1'),
            KeyboardButton(text='🌛 Internet paket-3')
        ],
        [
            KeyboardButton(text='🌛 Internet paket-6'),
            KeyboardButton(text='🌛 Internet paket-9')
        ],
        [
            KeyboardButton(text='🌛 Internet paket-12'),
            KeyboardButton(text='🌛 Internet paket-15')
        ],
        [
            KeyboardButton(text='🌛 Internet paket-20'),
            KeyboardButton(text='🌛 Internet paket-30')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ]
)
hafta_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Hafta 100 MB')
        ],
        [
            KeyboardButton(text='🗓 Hafta 400 MB')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)
kun_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌞 Kun 10 MB'),
            KeyboardButton(text='🌞 Kun 20 MB'),
        ],
        [
            KeyboardButton(text='🌞 Kun 30 MB'),
            KeyboardButton(text='🌞 Kun+ 150 MB'),
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)
g_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚀 «4G KUN»'),
            KeyboardButton(text='🚀 «4G OY»')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)