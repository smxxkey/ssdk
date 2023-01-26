import datetime
import telebot

TOKEN = "5835021046:AAF5AHmnDuS6666mkX8J4VykODGbdYTk6TM"
bot = telebot.TeleBot(TOKEN)

users = {} # dictionary to store user id and their balance

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    if user_id in users:
        bot.send_message(message.chat.id, "Снова привет, твой IQ: {}.".format(users[user_id]['balance']))
    else:
        users[user_id] = {'balance': 0, 'last_message_time': None}
        bot.send_message(message.chat.id, "Добро пожаловать, я IQ бот! Отныне твой IQ: 0.\n\nЗаходи завтра, чтобы его увеличить!")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    user = users[user_id]
    now = datetime.datetime.now()
    if user['last_message_time'] is not None:
        last_message_time = datetime.datetime.fromtimestamp(user['last_message_time'])
        if last_message_time.date() == now.date():
            bot.send_message(message.chat.id, "Вы уже пополняли свой IQ, заходите завтра.")
            return
    user['balance'] += 1
    user['last_message_time'] = now.timestamp()
    bot.send_message(message.chat.id, 'Ваш IQ вырос на 1, ваш IQ: {}'.format(user['balance']))

bot.polling()
