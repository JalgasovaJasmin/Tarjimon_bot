from transliterate import to_latin, to_cyrillic
import telebot
bot=telebot.TeleBot('8075182011:AAF4FwdRbLH9JGCHYeJ2DD3tA_Af9UdWRzQ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    xabar = f'🌝Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!🤗'
    xabar += '\n🖌Matningizni yuboring.'
    bot.reply_to(message, xabar)

@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob =to_latin(msg)
    bot.reply_to(message, javob)


bot.polling()


