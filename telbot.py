import datetime
import telebot
import cv2

artur_id = "239289123"
sofi_id = "870800205"
BOT_TOKEN = "888729683:AAGYwRwy2xrDuZnD8PtD9-v0S2aDhBh9r-g"
telebot.apihelper.proxy = {'https': "63.249.67.70:53281"}
bot = telebot.TeleBot(BOT_TOKEN)
print(bot.get_me())
# bot.send_photo(artur_id, open('/home/zico/PycharmProjects/untitled/photo/001.jpeg', "rb"))

