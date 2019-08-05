# encoding: utf-8
import time
import sys
import urllib, urllib3, base64
import json
import re

def get_token(API_Key,Secret_Key):
    # 获取access_token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_Key+'&client_secret='+Secret_Key
    request = urllib3.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib3.urlopen(request)
    content = response.read()
    content_json=json.loads(content)
    access_token=content_json['access_token']
    return access_token


if __name__ == '__main__':
    API_Key = "0XjjziGbG8ahFz8K6oVmXhh0"
    Secret_Key = "mXUApNu1qt9kktS3Rz2PhQ2qTZPu9gCb"
    filepath = "E:/ID/"
    filename="59.jpg"
    access_token=get_token(API_Key,Secret_Key)
    # recognition_word_high=recognition_word_high(filepath,filename,access_token)