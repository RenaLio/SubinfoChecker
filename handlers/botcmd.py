import os
import re
import time
import requests
import telebot
from datetime import datetime
from telebot import TeleBot
from telebot.types import Message
from handlers.subinfo import subinfo


def botinit(bot: TeleBot):
    bot.delete_my_commands(scope=None, language_code=None) #

    bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("subinfo", "查询机场订阅信息"),
            telebot.types.BotCommand("sub", "回复消息查询⬆"),
            telebot.types.BotCommand("help", "帮助菜单")
        ],
        # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
        # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
    )
    print('Bot初始化完成')


def botstart(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id,  f"您好`{message.from_user.first_name}`，您可以使用我来查询机场订阅信息",parse_mode='Markdown')

def bothelp(message: Message, bot: TeleBot):
    back_msg = bot.send_message(message.chat.id, f"  /subinfo <订阅链接>\n"
                                                 f" /sub[空格] 回复一条消息\n"
                                                 f" /ping 检查机器人是否工作")
    time.sleep(15)
    try:
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
    except:
        return

def get_subinfo(message: Message, bot: TeleBot):
    info_text = subinfo(message.text)
    try:
        bot.reply_to(message, info_text,parse_mode='Markdown')
    except:
        return

def get_sub(message: Message, bot: TeleBot):
    if message.reply_to_message == None:
        return
    back_msg = bot.send_message(message.chat.id, f" `正在查询...`", disable_notification=True,parse_mode='Markdown')
    info_text = subinfo(message.reply_to_message.text)
    try:
        bot.reply_to(message, info_text,parse_mode='Markdown')
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
    except:
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
        return

def get_dalay(message: Message, bot: TeleBot):
    start = datetime.now()
    # s1 = time.time()
    # msg_delay2 = s1-message.date
    message =  bot.reply_to(message,"pong~",disable_notification=True)
    end = datetime.now()
    msg_delay = (end-start).microseconds/1000
    bot.edit_message_text(f"pong~ | 消息延迟: `{msg_delay:.2f}ms`",message.chat.id,message.id,parse_mode='Markdown')