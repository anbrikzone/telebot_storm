import telebot
from telebot import types
from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(getenv("TOKEN_BOT"))

@bot.message_handler(commands=['start'])
def startBot(message):
    # first_message = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, hi! Do you want to know more?"
    first_message = f"Привет, Санька!"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_message, parse_mode="html", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_message = "Перейдем на сайт Google?"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Go to website", url="http://www.google.com"))
            bot.send_message(function_call.message.chat.id, second_message, reply_markup=markup)
            bot.answer_callback_query(function_call.id)

bot.infinity_polling()