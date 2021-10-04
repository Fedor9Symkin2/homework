import telebot
from telebot import types
from translate import Translator


bot = telebot.TeleBot(TOKEN)

users = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton('language')

    markup.add(item_1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'language':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_2 = types.KeyboardButton('English')
            item_3 = types.KeyboardButton('Russian')
            markup.add(item_2, item_3)
            bot.send_message(message.chat.id, 'Language', reply_markup=markup)

        elif message.text == 'English':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Back')
            markup.add(item_1)
            bot.send_message(message.chat.id, 'напищи мне что надо перевести', reply_markup=markup)

        elif message.text == 'Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_2 = types.KeyboardButton('English')
            item_3 = types.KeyboardButton('Russian')
            markup.add(item_2, item_3)
            bot.send_message(message.chat.id, 'Language', reply_markup=markup)

        elif message.text == 'Russian':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Back')
            markup.add(item_1)
            bot.send_message(message.chat.id, 'Russian', reply_markup=markup)




bot.polling(none_stop=True)