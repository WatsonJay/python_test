#!/usr/bin/env python
# -*- coding: cp936 -*-
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/11/27
# Created by 独自等待
# 博客 http://www.waitalone.cn/
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print('模块导入错误,请使用pip安装,pytesseract依赖以下库：')
    print('http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil')
    print('http://code.google.com/p/tesseract-ocr/')
    raise SystemExit

img = Image.open('./20191213101552.png','r')
img.load()
print(img)
vcode = pytesseract.image_to_string(img)
print(vcode)
print('okaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
