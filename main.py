import telebot
import json, os
from telebot import types

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='Понедельник', callback_data='monday')
    btn2 = types.InlineKeyboardButton(text='Вторник', callback_data='tuesday')
    btn3 = types.InlineKeyboardButton(text='Среда', callback_data='wednesday')
    btn4 = types.InlineKeyboardButton(text='Четверг', callback_data='thursday')
    btn5 = types.InlineKeyboardButton(text='Пятница', callback_data='friday')
    btn6 = types.InlineKeyboardButton(text='Суббота', callback_data='saturday')

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)

    bot.send_message(message.chat.id, 'Выберите день', reply_markup=markup)



@bot.callback_query_handler(func= lambda call: True)
def days(call):
    with open('schedule.json', 'r') as file:
        data = json.load(file)
    day = call.data
    day_lessons = data[day]

    text = f"🥲{day.capitalize()}:\n"

    for lesson in day_lessons:
        text += f"{lesson['subject']} в {lesson['time']} - {lesson['class']}\n"
    bot.send_message(call.message.chat.id, text)
    

bot.polling(none_stop=True)









