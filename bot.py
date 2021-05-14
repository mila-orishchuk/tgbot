import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from dotenv import load_dotenv
import logging
from service.db_service import DbService
from base import Session

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)

session = Session()
db = DbService(session)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, f"Приятно познакомиться, {message.from_user.first_name}.")
    await main_menu(message.chat.id)


async def main_menu(chat_id):
    markup_inline = types.InlineKeyboardMarkup()
    item_menu = types.InlineKeyboardButton(
        text='Меню на день', callback_data='menu')
    item_ingredients = types.InlineKeyboardButton(
        text='Ингредиенты', callback_data='ingredients')
    markup_inline.add(item_menu, item_ingredients)
    await bot.send_message(chat_id, '''Вы можете выбрать рецепты на завтрак, обед, ужин или с помощью имеющихся в 
вашем холодильнике ингредиентов подобрать рецепт''', reply_markup=markup_inline)


@dp.callback_query_handler(lambda call: call.data == "menu")
async def callback_worker(callback_query: types.CallbackQuery):
    markup_inline = types.InlineKeyboardMarkup()
    item_breakfast = types.InlineKeyboardButton(
        text='Завтрак', callback_data='breakfast')
    item_lunch = types.InlineKeyboardButton(
        text='Обед', callback_data='lunch')
    item_snack = types.InlineKeyboardButton(
        text='Перекус', callback_data='snack')
    item_dinner = types.InlineKeyboardButton(
        text='Ужин', callback_data='dinner')
    item_main = types.InlineKeyboardButton(
        text='Главная', callback_data='main')
    markup_inline.add(
        item_breakfast,
        item_lunch,
        item_snack,
        item_dinner,
        item_main
    )
    await bot.send_message(
        callback_query.message.chat.id, "Выберите один из предложенных вариантов",
        reply_markup=markup_inline
    )
    await callback_query.message.delete()


@dp.callback_query_handler(lambda call: call.data == "breakfast")
async def callback_main(callback_query: types.CallbackQuery):
    await db.get_random_recipe()


@dp.callback_query_handler(lambda call: call.data == "main")
async def callback_main(callback_query: types.CallbackQuery):
    await main_menu(callback_query.message.chat.id)
    await callback_query.message.delete()


@dp.callback_query_handler(lambda call: call.data == "ingredients")
async def callback_ingredient(callback_query: types.CallbackQuery):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_meat = types.KeyboardButton('Мясо, птица, яйца')
    item_fish = types.KeyboardButton('Рыба и морепродукты')
    item_vegetables = types.KeyboardButton('Овощи и зелень')
    item_fruits = types.KeyboardButton('Фрукты и ягоды')
    item_milk = types.KeyboardButton('Молочные продукты')
    item_cereal = types.KeyboardButton('Крупы, бобовые')
    item_pastry = types.KeyboardButton('Из теста')
    markup_reply.add(item_meat, item_fish, item_vegetables,
                     item_fruits, item_milk, item_cereal, item_pastry)
    await bot.send_message(
        callback_query.message.chat.id, 'Выберете ингредиенты из списка ниже: ', reply_markup=markup_reply)


if __name__ == '__main__':
    executor.start_polling(dp)
