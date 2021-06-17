# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 11:00
# @Author  : Jaywatson
# @File    : MD5.py
# @Soft    : python_test

import hashlib

str_src = 'TASC?O3RJMV?WDJKX?ZM'
str_md5 = 'e9032'

list_base = list('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

str_src = list(str_src)
for i in list_base:
    str_src[4] = i
    for j in list_base:
        str_src[11] = j
        for k in list_base:
            str_src[17] = k
            strtemp_md5 = str(hashlib.md5(''.join(str_src).encode("utf-8")).hexdigest())
            if (strtemp_md5[0:5] == str_md5):
                print(''.join(str_src), strtemp_md5)
                break