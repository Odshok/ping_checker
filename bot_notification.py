import telebot
#from telebot import types
import configparser
#import sys
#import random
from telebot import types




def bot_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get("Bot", "token")

def start(messages="Hello, World!!!"):
    token = bot_token()
    bot = telebot.TeleBot(token)
    id = "420359525" # id чата

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("🌡️ Температура")
#    markup.add(item1)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет')


    # @bot.message_handler(commands=['button'])
    # def button_message(message):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     item1 = types.KeyboardButton("🌡️ Температура")
    #     markup.add(item1)
    #     bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

    # @bot.message_handler(content_types='text')
    # def message_reply(message):
    #     if message.text == "🌡️ Температура":
    #         bot.send_message(message.chat.id, microtik_get.get_temp())

    bot.infinity_polling()

def send_error_message(message_text: str = "error"):
    token = bot_token()
    bot = telebot.TeleBot(token)
    id = "420359525" # id чата
    bot.send_message(id,message_text)

    #bot.send_message(id, messages)

    # def inso_sende(message):
    #   bot.send_message(message.chat.id,random.randint(0, 15))
    #
    # @bot.message_handler(commands=['start'])
    # def start_message(message):
    #     #bot.send_message(message.chat.id,random.randint(0, 15))
    #     bot.send_message(id, random.randint(0, 15))
    #
    # @bot.message_handler(commands=['woow'])
    # def woow_message(message):
    #   bot.send_message(message.chat.id,"woow ✌️ ")
    #


    #bot.polling(none_stop=True)

