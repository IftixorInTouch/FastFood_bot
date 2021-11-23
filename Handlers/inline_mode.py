from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, \
    InlineKeyboardButton

from data import dp, db
from callback_datas import buy_callback


@dp.inline_handler(text="")
async def testing(query: InlineQuery):
    results = []
    foods = await db.select_foods()
    for food in foods:
        results.append(
            InlineQueryResultArticle(
                id=str(food[0]),
                title=food[1],
                description=str(food[2]),
                thumb_url=food[3],
                input_message_content=InputTextMessageContent(
                    message_text=f"{food[1]} по цене {food[2]}"
                ),
                reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Добавить в корзину",
                                             callback_data=buy_callback.new(item_name=food[1], price=food[2]))
                    ]
                ]
                )
            )
        )
    await query.answer(results=results, cache_time=15)
