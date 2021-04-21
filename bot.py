
import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_menu = types.InlineKeyboardButton(
        text='Меню на день', callback_data='menu')
    item_ingredients = types.InlineKeyboardButton(
        text='Ингредиенты', callback_data='ingredients')
    markup_inline.add(item_menu, item_ingredients)
    bot.send_message(
        message.chat.id, f"Приятно познакомиться, {message.from_user.first_name}.\nВы можете выбрать рецепты на завтрак, обед, ужин или с помощью имеющихся в вашем холодильнике ингредиентов подобрать рецепт", reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "menu":
        markup_inline = types.InlineKeyboardMarkup()
        item_breakfast = types.InlineKeyboardButton(
            text='Завтрак', callback_data='breakfast')
        item_lunch = types.InlineKeyboardButton(
            text='Обед', callback_data='lunch')
        item_snack = types.InlineKeyboardButton(
            text='Перекус', callback_data='snack')
        item_dinner = types.InlineKeyboardButton(
            text='Ужин', callback_data='dinner')
        markup_inline.add(item_breakfast, item_lunch, item_snack, item_dinner)
        bot.send_message(
            call.message.chat.id, "Выберите один из предложенных вариантов", reply_markup=markup_inline)
    elif call.data == "ingredients":
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
        bot.send_message(
            call.message.chat.id, 'Выберете ингредиенты из списка ниже: ', reply_markup=markup_reply)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "breakfast":
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите один из предложенных вариантов",
                                  reply_markup=None)

    except Exception as err:
        print(err)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print('work')

    if message.text == 'Завтрак':
        bot.send_message(message.chat.id, f'')
    elif message.text == 'Обед':
        pass


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()