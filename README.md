# 订阅信息查询 Telegram Bot

## DEMO

[@Thesubinfo2_bot](https://t.me/Thesubinfo2_bot)

## 安装教程

先去botfather获取bot token，然后在vps内使用一下命令安装bot

```
git clone https://github.com/RenaLio/SubinfoChecker
```


### Debian | Ubuntu:

```
apt-get upgrade -y 
apt install -y python3 python3-pip 
pip3 install -r requirements.txt
```

### CentOS 

```
yum update -y
yun install -y python3 python3-pip
pip3 install -r requirements.txt
```

### 运行方式

直接使用Python命令调用Bot即可

```
python3 subinfo.py
```

建议使用`screen`、`systemd`、`PM2`等工具将Bot挂在后台运行。

## 其他

### subinfo1.py

> 推荐个人使用，直接发送`订阅链接`就可以返回结果

### subinfo2.py

> `/subinfo URL`
