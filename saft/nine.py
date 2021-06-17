# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 10:22
# @Author  : Jaywatson
# @File    : nine.py
# @Soft    : python_test

#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值

import sys
data = input("input:")
if (len(data)%2 != 0):
    print('数据长度有误')
    sys.exit()
dict = {'1':'','2':'a','3':'d','4':'g','5':'j','6':'m','7':'p','8':'t','9':'w'}
str_flag=''
code=0
for index, everyChar in enumerate(data):
    if index%2 ==0:
        code = ord(dict[everyChar])
    elif index%2 != 0 and int(everyChar)<4:
        str_flag += chr(code+int(everyChar)-1)
    else:
        print("字符大小超出限制")
        break
print('word: ' + str_flag)