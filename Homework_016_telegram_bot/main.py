import telebot
import datetime

API_TOKEN = '**********:AAGaNq8MIT6dpHDRw6LIaPYAXZTv8kpJ5cs'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Бот gurvik приветствует вас! '
                          'Благодарю, что решили воспользоваться моими услугами!')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Чем могу помочь? '
                          'Пожалуйста задайте ваш вопрос моему админу.')


@bot.message_handler(commands=['time'])
def send_time(message):
    time_now = datetime.datetime.now().time()
    bot.reply_to(message, time_now.strftime('%H:%M:%S'))


@bot.message_handler(commands=['date'])
def send_date(message):
    date_now = datetime.datetime.now().date()
    bot.reply_to(message, str(date_now))


@bot.message_handler(content_types=['text'])
def send_bad_words(message):
    message_text = str(message.text.lower())
    if 'блин' in message_text:
        bot.reply_to(message, 'Не используйте ненормативную лексику!')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, 'Новости у нас всегда хорошие!')


bot.infinity_polling()
