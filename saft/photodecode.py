# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 9:41
# @Author  : Jaywatson
# @File    : photodecode.py
# @Soft    : python_test
#jpg 文件基本以ffd8开头，fff9结尾
file_src = open('./WHOAMI.jpg','rb')
file_dst = open('./flag.jpg','wb')
data_img = file_src.read()[::-1]
file_dst.write(data_img)
file_src.close()
file_dst.close()