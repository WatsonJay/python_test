import cv2 as cv
import os
import time

# 替换字符列表
ascII_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascII_char)

#加载视频
name = input("输入视频地址：")
cap=cv.VideoCapture(name)
while True:
    #读取视频每一帧
    hashFrame,frame=cap.read()
    if not hashFrame:
        print("读取错误！")
        break
    #视频长度
    height = frame.shape[0]
    width = frame.shape[1]
    #转灰度图
    img_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    img_resize = cv.resize(img_gray,(int(width/10),int(height/10)))
    text=''
    #遍历图片中的像素
    for row in img_resize:
        for pixel in row:
            #根据像素值，选取对应的字符
            text += ascII_char[int(pixel/256*char_len)]
        text += '\n'
    #清屏
    os.system('cls') #mac是clear
    #输出生成的字符方阵
    print(text)
    time.sleep(0.03)
