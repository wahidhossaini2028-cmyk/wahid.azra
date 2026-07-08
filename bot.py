import telebot

bot = telebot.TeleBot("8841578411:AAGZXTIoGHdctDCz51w1L32Aztb4xIWZpVE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات شما فعال است.")

bot.polling()