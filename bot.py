import config
import telebot
import sqlite3

# Настраиваем соединение с нашим ботом
bot = telebot.TeleBot(config.token)

#Бот отвечает на команды
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Ёу, чел")
#Бот отвечает на все сообщения по умолчанию
def echo_all(message):
    bot.reply_to(message, message.text)

#Запускаем бота
bot.polling()



