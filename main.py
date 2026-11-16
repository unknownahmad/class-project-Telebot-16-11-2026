import telebot
import random
import os
from dotenv import load_dotenv
from AI_s import abuse_AI
#
base_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(base_dir, '.env'))
TOKEN = os.getenv('BOT_TOKEN')

file_path = os.path.join(base_dir, 'countries.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    countries = [line.strip() for line in f if line.strip()]

numbers_path = os.path.join(base_dir, 'numbers.txt')
with open(numbers_path, 'r', encoding='utf-8') as f:
    numbers = [line.strip() for line in f if line.strip()]

bot = telebot.TeleBot(TOKEN)
print('hey')
#---

#start command
@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.chat.id
    bot.send_message(user,'Hello \n you cracket!!! ')
ai_users = set()
#main code
@bot.message_handler(content_types=['text'])
def send_text(message):
    user = message.chat.id
    
    if message.text == "help":
        bot.send_message(user,'⛄⛄⛄⛄⛄ cracker ⛄⛄⛄⛄⛄')

    elif message.text == '🤍':
        bot.send_message(user, '⛄⛄⛄⛄')
    elif message.text=='how are you?':
         bot.send_message(user,'Huh?')
         bot.send_message(user,'why you asking, mind your bisuness')
    elif message.text == 'country':
        random_country = random.choice(countries)
        bot.send_message(user, random_country)
    elif message.text== 'number':
        random_number = random.choice(numbers)
        bot.send_message(user, random_number)
    elif  message.text == 'i want to talk to ai':
        ai_users.add(user)
        reply = abuse_AI(message.text)
        bot.send_message(user, reply)
    elif message.text == 'bye':
        ai_users.discard(user)
        bot.send_message(user, 'well')
        bot.send_message(user, 'see you')
    elif user in ai_users:
        reply = abuse_AI(message.text)
        bot.send_message(user, reply)
    else:
        bot.send_message(message.chat.id, 'hahaha ¯\_(ツ)_/¯ ')


bot.infinity_polling()
