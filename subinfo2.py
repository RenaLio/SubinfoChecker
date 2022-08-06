import os
import re
import time
import requests
import telebot
from datetime import datetime

# API_KEY = os.environ['token']
# API_KEY = os.getenv('API_KEY')

API_KEY = "<YOUR BOT TOKEN>"
bot = telebot.TeleBot(API_KEY)

def botinit():
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


def convert_time_to_str(time):
    # 时间数字转化成字符串，不够10的前面补个0
    if (time < 10):
        time = '0' + str(time)
    else:
        time = str(time)
    return time


def sec_to_data(y):
    h = int(y // 3600 % 24)
    d = int(y // 86400)
    h = convert_time_to_str(h)
    d = convert_time_to_str(d)
    return d + "天" + h + '小时'


def StrOfSize(size):
    def strofsize(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return strofsize(integer, remainder, level)
        elif integer < 0:
            integer = 0
            return strofsize(integer, remainder, level)
        else:
            return integer, remainder, level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = strofsize(size, 0, 0)
    if level + 1 > len(units):
        level = -1
    return ('{}.{:>03d} {}'.format(integer, remainder, units[level]))


def subinfo(url):
    headers = {'User-Agent': 'ClashforWindows/0.18.1'}
    try:
        message_raw = url
        final_output = ''
        url_list = re.findall("https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
                              message_raw)  # 使用正则表达式查找订阅链接并创建列表
        for url in url_list:
            try:
                res = requests.get(url, headers=headers, timeout=5)  # 设置5秒超时防止卡死
            except:
                final_output = final_output +'订阅链接：`' + url + '`\n连接错误' + '\n\n'
                continue
            if res.status_code == 200:
                try:
                    info = res.headers['subscription-userinfo']
                    info_num = re.findall('\d+', info)
                    time_now = int(time.time())
                    output_text_head = '订阅链接：`' + url + '`\n已用上行：`' + StrOfSize(
                        int(info_num[0])) + '`\n已用下行：`' + StrOfSize(int(info_num[1])) + '`\n剩余：`' + StrOfSize(
                        int(info_num[2]) - int(info_num[1]) - int(info_num[0])) + '`\n总共：`' + StrOfSize(
                        int(info_num[2]))
                    if len(info_num) == 4:
                        timeArray = time.localtime(int(info_num[3]) + 28800)
                        dateTime = time.strftime("%Y-%m-%d", timeArray)
                        if time_now <= int(info_num[3]):
                            lasttime = int(info_num[3]) - time_now
                            output_text = output_text_head + '`\n过期时间：`' + dateTime + '`\n剩余时间：`' + sec_to_data(
                                lasttime) + '`'
                        elif time_now > int(info_num[3]):
                            output_text = output_text_head + '`\n此订阅已于`' + dateTime + '`过期！'
                    else:
                        output_text = output_text_head + '`\n到期时间：`没有说明捏`'
                except:
                    output_text = '订阅链接：`' + url + '`\n无流量信息捏'
            else:
                output_text = '订阅链接：`' + url + '`\n无法访问\n'
            final_output = final_output + output_text + '\n\n'
        return (final_output)
    except:
        return ('参数错误')

@bot.message_handler(commands=['start'],func=lambda message:message.chat.type == "private")
def start(message):
    bot.send_message(message.chat.id,  f"您好`{message.from_user.first_name}`，您可以使用我来查询机场订阅信息",parse_mode='Markdown')


@bot.message_handler(commands=["help"])
def help(message):
    back_msg = bot.send_message(message.chat.id, f" /subinfo <订阅链接>\n"
                                                 f" /sub[空格] 回复一条消息\n"
                                                 f" /ping 检查机器人是否工作")
    time.sleep(15)
    try:
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
    except:
        return

@bot.message_handler(commands=['subinfo'])
def get_subinfo(message):
    info_text = subinfo(message.text)
    try:
        bot.reply_to(message, info_text,parse_mode='Markdown')
    except:
        return

@bot.message_handler(commands=['sub'])
def get_sub(message):
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

@bot.message_handler(commands=['ping'])
def get_dalay(message):
  start = datetime.now()
  # s1 = time.time()
  # msg_delay2 = s1-message.date
  message =  bot.reply_to(message,"pong~",disable_notification=True)
  end = datetime.now()
  msg_delay = (end-start).microseconds/1000
  bot.edit_message_text(f"pong~ | 消息延迟: `{msg_delay:.2f}ms`",message.chat.id,message.id,parse_mode='Markdown')


if __name__ == '__main__':
    botinit()
    bot.polling(none_stop=True)
