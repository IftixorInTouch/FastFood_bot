from data import dp, db
from aiogram.types import Message, CallbackQuery
from Keyboards.inline_keyboards import beginning


@dp.message_handler(commands=["start"])
async def start_keyboard(message: Message):
    user_id = message.from_user.id
    existing_user = await db.select_user(user_id)
    if not existing_user:
        username = message.from_user.username
        first_name = message.from_user.last_name
        last_name = message.from_user.first_name
        await db.add_user(username=username, user_id=user_id, first_name=first_name, last_name=last_name)
    await message.answer("Нажмите на меню чтобы увидеть меню", reply_markup=beginning)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Все заказы были отменены!", show_alert=True)
