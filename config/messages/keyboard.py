from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Definición de botones
startbutton = InlineKeyboardMarkup([
    [InlineKeyboardButton("Next", callback_data="nextstart")],
])

comandsbutton = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Gateways", callback_data="gateways"),
        InlineKeyboardButton("Tools", callback_data="tools"),
        InlineKeyboardButton("Webtools", callback_data="webtools")
    ],
    [
      InlineKeyboardButton("Close", callback_data="finbtn")
    ],
])

gatewayslistbtn = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Free", callback_data="fregatewaylist"),
        InlineKeyboardButton("Premium", callback_data="premiumgatewaylist")
    ],
    [
      InlineKeyboardButton("Close", callback_data="finbtn")
    ],
])