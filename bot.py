import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8496169188:AAG2etS3LpZftFTq-XEoI4Q_xeodLYW27m4"  
GAME_URL = "https://netlify.app"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Запустить Симулятор", 
                web_app=WebAppInfo(url=GAME_URL)
            )
        ]
    ])
    
    welcome_text = (
        f"Привет, {message.from_user.first_name}! 🏭\n\n"
        "Добро пожаловать в симулятор конструкторского бюро!\n"
        "Собирай ресурсы, прокачивай свой завод, совершай тестовые запуски "
        "и копи монеты для вывода реальных подарков совершенно бесплатно!\n\n"
        "Нажми кнопку ниже, чтобы запустить игру прямо сейчас 👇"
    )
    
    await message.answer(text=welcome_text, reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
