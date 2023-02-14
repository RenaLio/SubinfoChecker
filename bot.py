from handlers import botcmd
from telebot import TeleBot
import toolbox 

def register_handlers():
    bot.register_message_handler(botcmd.botstart, commands=['start'], pass_bot=True)
    bot.register_message_handler(botcmd.bothelp, commands=['help'], pass_bot=True)
    bot.register_message_handler(botcmd.get_subinfo, commands=['subinfo'], pass_bot=True)
    bot.register_message_handler(botcmd.get_sub, commands=['sub'], pass_bot=True)
    bot.register_message_handler(botcmd.get_dalay, commands=['ping'], pass_bot=True)

def run():
    botcmd.botinit(bot)
    bot.polling(none_stop=True)

if __name__ == '__main__':
    args=toolbox.init()
    API_KEY = args.token
    bot = TeleBot(API_KEY)
    register_handlers()
    run()