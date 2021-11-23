from aiogram import Dispatcher, Bot
from Database.users import Database
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
db = Database()
