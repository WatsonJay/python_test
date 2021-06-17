# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 11:59
# @Author  : Jaywatson
# @File    : math_sum.py
# @Soft    : python_test

def avg(list=[]):
  try:
     return sum(list) / len(list)
  except:
      return 0

def colnum_to_colname(colnum):
    if type(colnum) is not int:
        return colnum
    str = ''
    colnum += 1
    while (not (colnum // 26 == 0 and colnum % 26 == 0)):
        temp = 25
        if (colnum % 26 == 0):
            str += chr(temp + 65)
        else:
            str += chr(colnum % 26 - 1 + 65)
        colnum //= 26
    return str[::-1]

def colname_to_colnum(colname):
    if type(colname) is not str:
        return colname
    col = 0
    power = 1
    for i in range(len(colname)-1,-1,-1):
        ch = colname[i]
        col += (ord(ch)-ord('A')+1)*power
        power *= 26
    return col-1

# 获取字符串长度，一个中文的长度为2
def len_byte(value):
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)