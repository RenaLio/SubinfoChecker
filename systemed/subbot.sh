[Unit]
After=network.target
Description=Subinfo Bot

[Service]
Type=simple
WorkingDirectory=/root/SubinfoChecker /
ExecStart=/usr/bin/python3 bot.py -t Token
Restart=always

[Install]
WantedBy=multi-user.target