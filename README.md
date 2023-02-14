# 订阅信息查询 Telegram Bot

## DEMO

[@Thesubinfo2_bot](https://t.me/Thesubinfo2_bot)

## 配置

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
python3 bot.py -t 123456:xxxxxxxx
```

`123456:xxxxxxxxxxx`为bot token

建议使用`screen`、`systemd`、`PM2`等工具将Bot挂在后台运行。

## 安装方式

### 持久化

- Systemed

  ```
  bash install.sh
  ```

  查看状态

  ```
  systemctl status subbot
  ```

  查看日志

  ```
  journalctl -u subbot
  ```

  启动 

  ```
  systemctl start subbot
  ```

  停止 

  ```
  systemctl stop subbot
  ```

  重启 

  ```
  systemctl restart subbot
  ```

  杀死所有子进程

  ```
  systemctl kill subbot
  ```

## 其他

### subinfo.py

> 推荐个人使用，直接发送`订阅链接`就可以返回结果

### subinfo2.py

> `/subinfo URL`

## 感谢

subinfo的主要代码来源自`telegram-PGM`模块