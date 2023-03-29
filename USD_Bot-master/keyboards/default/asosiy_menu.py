from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🟡 Beeline'),
            KeyboardButton(text='🟣 Ucell')
        ],
        [
            KeyboardButton(text='🔵 Uzmobile'),
            KeyboardButton(text='🔻 MobiUz')
        ]
    ],resize_keyboard=True
)
asosiy_ichi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📔 Tariflar'),
            KeyboardButton(text='🌏 Internet')
        ],
        [
            KeyboardButton(text='🏠 Bosh menu'),
            KeyboardButton(text='📁 Boshqa hizmatlar')
        ]
    ],resize_keyboard=True
)
usel_asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗒 Tariflar'),
            KeyboardButton(text='🌐 Internet')
        ],
        [
            KeyboardButton(text='💬 Boshqa xizmatlar'),
            KeyboardButton(text='🏠 Bosh menu')
        ],
    ],resize_keyboard=True

)
uzmobile_asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Tariflar'),
            KeyboardButton(text='🛸 Internet')
        ],
        [
            KeyboardButton(text='🛠 Boshqa xizmatlar'),
            KeyboardButton(text='🏠 Bosh menu')
        ]
    ],resize_keyboard=True
)
mobiuz_asosiy= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📕 Tariflar'),
            KeyboardButton(text='📶 Internet')
        ],
        [
            KeyboardButton(text='📚 Boshqa xizmatlar'),
            KeyboardButton(text='🏠 Bosh menu')
        ]
    ],resize_keyboard=True
)
