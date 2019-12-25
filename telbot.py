import datetime
import telebot
import cv2



telebot.apihelper.proxy = {'https': "63.249.67.70:53281"}
bot = telebot.TeleBot(BOT_TOKEN)
print(bot.get_me())
# bot.send_photo(artur_id, open('/home/zico/PycharmProjects/untitled/photo/001.jpeg', "rb"))

