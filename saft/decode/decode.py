# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 11:19
# @Author  : Jaywatson
# @File    : decode.py
# @Soft    : python_test

file1 = open('./密文.txt','rb')
file2 = open('./密钥.txt','rb')
data_word = file1.read()
data_key = file2.read()
temp=''
for i in range(len(data_word)):
    temp += chr(data_word[i]^data_key[i])
print(temp)