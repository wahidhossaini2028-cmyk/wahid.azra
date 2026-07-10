import telebot
import re

TOKEN = "8841578411:AAHRrGxw9fQn8r1Dg2AW2NIn7wreEaVPQrc"

bot = telebot.TeleBot(TOKEN)

# Detect links
LINK_PATTERN = r"(https?://\S+|www\.\S+|t\.me/\S+)"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running.")

@bot.message_handler(func=lambda message: True)
def delete_links(message):
    if message.text and re.search(LINK_PATTERN, message.text):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            print(f"Deleted a link from {message.from_user.first_name}")
        except Exception as e:
            print(e)

print("Bot started...")
bot.infinity_polling()bot.polling() 