# -*- coding: utf-8 -*-
import time
import sys
import requests
import urllib, base64
from urllib import request
from urllib import parse
import pyHook
import pythoncom
from win32api import GetSystemMetrics as gsm
import json
import re

# 提前绑定鼠标位置事件
from PIL import Image,ImageGrab

#创建全局变量，以便储存鼠标Down 和 Up 时的坐标
positionDown = ()
position = ()
full = False
hm = None


def get_token(API_Key,Secret_Key):
    # 获取access_token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_Key+'&client_secret='+Secret_Key
    req = request.Request(host)
    req.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = request.urlopen(host)
    content = response.read()
    content_json=json.loads(content)
    access_token=content_json['access_token']
    return access_token

def recognition_word_high(filepath,filename,access_token):
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(filepath + filename, 'rb')  # 二进制方式打开图文件
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = parse.urlencode(params).encode('utf-8')
    req = request.Request(url, params)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = request.urlopen(req)
    content = response.read()
    if (content):
        # print(content)
        world=re.findall('"words": "(.*?)"}',str(content),re.S)
        for each in world:
            print(each)


#鼠标左键按下触发
def onMouseEventDown(event):
    if event.MessageName == "mouse left down":
        print("MessageName:", event.MessageName)
        global positionDown
        positionDown = event.Position
    return True
#鼠标左键松开触发
def onMouseEventUp(event):
    if event.MessageName == "mouse left up":
        print("MessageName:", event.MessageName)
        global positionDown
        global position
        position = positionDown + event.Position
    return True

#截屏方法
def  printScreen(position):
    im = ImageGrab.grab(position)
    im.save('printscreen.jpg')
    recognize()
    return True

#获取键盘值方法
def onKeyboardEvent(event):
    if(event.Key=='Space'):
        global position
        if position is not None:
            printScreen(position)
    return True


def capture():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.MouseAllButtonsDown = onMouseEventDown
    hm.MouseAllButtonsUp = onMouseEventUp
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()

def recognize():
    API_Key = "0XjjziGbG8ahFz8K6oVmXhh0"
    Secret_Key = "mXUApNu1qt9kktS3Rz2PhQ2qTZPu9gCb"
    filepath = ""
    filename = "printscreen.jpg"
    access_token = get_token(API_Key, Secret_Key)
    recognition_word = recognition_word_high(filepath, filename, access_token)

if __name__ == '__main__':
    capture()
