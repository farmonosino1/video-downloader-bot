from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("🇷🇺 Русский", callback_data='ru'),
    InlineKeyboardButton("🇬🇧 English", callback_data='en'),
    InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='uz'),
)