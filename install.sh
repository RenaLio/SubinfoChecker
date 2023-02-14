#!/usr/bin/env bash

pip3 install -r requirements.txt
systemctl stop subbot
rm -rf /var/log/journal/*
chmod 755 subbot.service

CUSTOM_ARGS=""
read -ep " 请输入密钥:" password
CUSTOM_ARGS="${CUSTOM_ARGS} --token $password"

echo "[ 06/12 ] 创建进程守护文件"
	cat >/etc/systemd/system/subbot.service <<EOF
[Unit]
After=network.target
Description=Subinfo Bot

[Service]
Type=simple
WorkingDirectory=/root/SubinfoChecker /
ExecStart=/usr/bin/python3 bot.py -t $CUSTOM_ARGS
Restart=always

[Install]
WantedBy=multi-user.target
EOF


systemctl daemon-reload
systemctl start subbot
systemctl enable subbot