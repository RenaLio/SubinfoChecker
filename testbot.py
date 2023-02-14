from handlers import botcmd
from telebot import TeleBot
import toolbox 

def register_handlers():
    bot.register_message_handler(botcmd.get_dalay, commands=['ping'], pass_bot=True)
    bot.register_message_handler(botcmd.get_sub, content_types=["text"], pass_bot=True)

def run():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    args=toolbox.init()
    API_KEY = args.token
    bot = TeleBot(API_KEY)
    register_handlers()
    run()