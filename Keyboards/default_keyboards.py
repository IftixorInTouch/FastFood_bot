from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

form = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [
                                   KeyboardButton("Контакт", request_contact=True),
                                   KeyboardButton("Геолокация", request_location=True)
                               ]
                           ]
                           )
