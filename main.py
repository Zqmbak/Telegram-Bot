import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8685362521:AAEH1XGog2u5NqYeR6OxLb6kwkZvpcZ4m6c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Записаться!")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие..."  # подсказка в поле ввода
)

menu_uslugi = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Борода")],
        [types.KeyboardButton(text="Стрижка")],
        [types.KeyboardButton(text="Укладка")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие..."  # подсказка в поле ввода
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в барбершоп (Барби)!\n\n"
        "Выбери действие в меню ниже:",
        reply_markup=menu_keyboard
    )

@dp.message(lambda m: m.text == "Записаться!")
async def book(message: types.Message):
    reply_markup=menu_uslugi

@dp.message(lambda m: m.text == "Борода")
async def Boroda(message: types.Message):
    await message.answer("ОООО, Так ты Дворф!!!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())