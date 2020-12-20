#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import argv
import os
import telebot

path, key, user_id, ip = argv


bot = telebot.TeleBot(key)
start_msg = "Hello! Your stand is up.\nIP:"+str(ip)+"\nIf you want to stop stand, write me \"stand off\""


markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtnoff = telebot.types.KeyboardButton('stand off')
itembtnip = telebot.types.KeyboardButton('ip')
markup.row(itembtnoff)
markup.row(itembtnip)

bot.send_message(user_id, start_msg, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if str(message.from_user.id) == str(user_id):
	    if message.text == "stand off":
	    	bot.send_message(user_id, 'OK')
	    	os._exit(0)
	    if message.text == "ip":
	    	bot.send_message(user_id, ip)
        #ip = get('https://api.ipify.org').text
        #bot.send_message(message.from_user.id, 'My public IP address is: {}'.format(ip))
bot.polling()
