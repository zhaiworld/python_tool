# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os, subprocess, platform, io
import socket

from pyqrcode import QRCode

OS = platform.system()
"""方便将本地文件传输到手机端

日常工作中更多中地用于安卓、iOS多设备安装本地测试包。

前提
-- 1. 本地电脑上安装并配置了python开发环境
-- 2. 本地电脑开启代理，手机端配置了该代理IP

使用场景：

-- 1. 将该脚本下载到 .apk 或.ipa 文件 相同目录下
-- 2. 执行该.py   python file.py 
-- 3. 手机扫描二维码即可访问   或者 直接在浏览器访问 本地IP:8000

"""

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
        return ip


def run_server():
    cmd2 = "python -m SimpleHTTPServer 8000"
    cwd = os.getcwd()
    tmp = subprocess.Popen(cmd2, cwd=cwd)
    tmp.wait()


def get_QR(picDir=None):
    picDir = picDir or 'QR.png'
    qr_storage = io.BytesIO()
    ip = get_host_ip()
    ip_address = ip + ":8000"
    qr_code = QRCode(ip_address)
    qr_code.png(qr_storage, scale=10)
    with open(picDir, 'wb') as f:
        f.write(qr_storage.getvalue())
        print_qr(picDir)


def print_qr(fileDir):
    if OS == 'Darwin':
        subprocess.call(['open', fileDir])
    elif OS == 'Linux':
        subprocess.call(['xdg-open', fileDir])
    else:
        os.startfile(fileDir)


def env():
    count = 3
    while count:
        try:
            import pyqrcode
            break
        except:
            os.system("pip install pyqrcode")
            count -= 1
            continue


if __name__ == '__main__':
    env()
    run_server()
    get_QR()
