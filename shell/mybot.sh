#!/usr/bin/env bash

red() {
    echo -e "\033[31m\033[01m$1\033[0m"
}

green() {
    echo -e "\033[32m\033[01m$1\033[0m"
}

yellow() {
    echo -e "\033[33m\033[01m$1\033[0m"
}

screenName="mybot"
# 退出screen中原来的bot.py
screen -S mybot -X stuff  `echo -e '\003'`
# 在screen存在的基础上输入命令
screen -S $screenName -X stuff 'cd /root/SubinfoChecker &&python3 mybot.py'`echo -ne '\015'`
# # # 删除旧的screen
# # screen -S $screenName -X quit || red "没有找到 $screenName 的会话"
