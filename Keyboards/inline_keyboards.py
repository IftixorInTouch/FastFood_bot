from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

beginning = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Меню", switch_inline_query_current_chat="")
                                     ],
                                     [
                                         InlineKeyboardButton(text="Корзина", callback_data="basket"),
                                         InlineKeyboardButton(text="Отмена", callback_data="cancel")
                                     ]
                                 ])
