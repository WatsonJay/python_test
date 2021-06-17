# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 18:36
# @Author  : Jaywatson
# @File    : test.py
# @Soft    : hello_world
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrom_options = Options()
chrom_options.add_argument('--headless')

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'chromedriver.exe',chrome_options=chrom_options)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
time.sleep(3)
print(wd.title)