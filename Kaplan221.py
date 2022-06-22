import telebot
from telebot import types
import random
from songspy import a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6
from token1 import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    msg1 = "Привіт, я бот для пісень великого Юри Каплана. Я буду радити різні його пісні для тебе"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton("/help")
    markup.add(itembtn1)
    bot.send_message(message.chat.id, msg1, reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_command(message):
    markup = types.ReplyKeyboardRemove()
    msg2 = f"Ось мої команди: \n/sad\n/fun \n/rand"
    bot.send_message(message.chat.id, msg2, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def user_messages(message):
    if message.text == "/debug":
        bot.send_message(message.chat.id, message)
    elif message.text == "/sad":
        songs = [a1, a2, a3, a4, a5, a6, a7, a8]
        rand = random.randint(0, 7)
        print(songs[rand])
        bot.send_audio(message.chat.id, songs[rand])
    elif message.text == "/fun":
        songs2 = [b1, b2, b3, b4, b5, b6]
        rand1 = random.randint(0, 5)
        print(songs2[rand1])
        bot.send_audio(message.chat.id, songs2[rand1])
    elif message.text == "/rand":
        randomsongs = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6]
        rand1 = random.randint(0, 13)
        print(randomsongs[rand1])
        bot.send_audio(message.chat.id, randomsongs[rand1])  # randomsongs[rand1]
    else:
        bot.send_message(message.chat.id, "Error 404")


@bot.message_handler(content_types=["audio"])
def audiomess(message):
    if message.audio:
        bot.get_file(message.audio.file_id)
        bot.send_message(message.chat.id, message.audio.file_id)


bot.infinity_polling()
