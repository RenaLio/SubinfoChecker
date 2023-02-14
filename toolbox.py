import argparse

def init():
    parser = argparse.ArgumentParser(description='命令行参数')
    parser.add_argument('--token', '-t', type=str, help='机器人token,类如：123456: xxxxxxx', required=True)
    return parser.parse_args()