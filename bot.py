import telebot
from telebot import types
import time
from config import get_config
API_TOKEN  = get_config()['API_TOKEN']

_bot = telebot.TeleBot(API_TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_bounty_id = types.KeyboardButton('B',)
btn_campaigns = types.KeyboardButton('C')
btn_challenges = types.KeyboardButton('D')
btn_news = types.KeyboardButton('N')
btn_link = types.KeyboardButton('R')

markup_menu.add(btn_bounty_id, btn_campaigns, btn_challenges,btn_news, btn_link)

@_bot.message_handler(commands=['start'])
def send_welcome(message):
    #print('incoming message \n ', message)
    #print('...............def ......')

    _bot.send_message(message.chat.id, "Oh, hi there! Nice to meet you, " + message.from_user.first_name +
                      "\n")

@_bot.message_handler(commands=['help'])
def send_help(message):
    _bot.send_message(message.chat.id," Hello " + message.from_user.first_name +
    " Please click on the button to know about us or please click on the link")

@_bot.message_handler(commands=['location'])
def send_location(message):
    _bot.send_location(message.chat.id,50.9375, 6.9603)


@_bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'N':
	    _bot.send_message(message.chat.id, "EXAMPLE: \n\n" +
                                "Newa about telegram bot",reply_markup=markup_menu)

    elif message.text == "B":
        _bot.send_message(message.chat.id, "The Telegram user ID that you will need to be part of our campaign is: " 
           + str(message.chat.id) + "\n", reply_markup=markup_menu)

    elif message.text == "C":
        _bot.send_message(message.chat.id, "Here is a quick overview of our campaigns:\n\n", reply_markup=markup_menu)
    elif message.text == "R":
        _bot.send_message(message.chat.id, "https://www.linkedin.com/in/sumanadr1/" + str(message.chat.id), reply_markup=markup_menu)

    elif message.text == "D":
        _bot.send_message(message.chat.id,"Oh! Currently there is no active challenge!", reply_markup=markup_menu)

    else:
        _bot.send_message(message.chat.id, "Welcome to my page!!Please type /start or /help to know more about app or to get help from us and"+
               " type /location to get current location.")

def start():
    print('starting application')
    _bot.polling()