# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 19:43
# @Author  : Jaywatson
# @File    : zhengze.py
# @Soft    : python_test


import re
import os
import csv

name = "nohup"  # 这里自己输入文件名字,例如我们要处理ab.txt文件，此处name = "ab", 该写法需要将txt文件和该脚本放在同一目录下
txtName = name + ".out"
csvName = name + ".csv"

fp = open(txtName, "rb")  # 打开txt文本
a = fp.read()  # 读取xt文本
result = re.findall('----------------objectId:.*columnName: .*propertyId: (.*)------------------', a.decode('utf-8'))  # 正则匹配
list1 = []  # 该列表用于临时存储字符串
for i in result:  # 匹配到的内容逐条提取
    if i != '':  # 过滤空白字符
        print(i)  # 看匹配到的内容
        list1.append(i)  # 将字符串添加到列表再写进去，不然字符会被拆开成一个一个
        # 下面就是写入csv文件的功能了，newline=''可以避免空行问题
        with open(csvName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list1)
        list1.pop()  # 写入完成要将列表中的字符串删除